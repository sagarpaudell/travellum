import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Place, Major_Attraction, Things_To_Do, Review
from guides.models import Guide
from travellers.models import Traveller
from notifications.models import Notification
from accounts.models import User

def places(request):
    current_user=request.user
    if current_user.is_authenticated:
        traveller_user_logged_in= get_object_or_404(Traveller, email=current_user)
        notifications = Notification.objects.all().filter(receiver_email=current_user)
        places = Place.objects.all()
        context = {
            'places':places,
            'notifications': notifications,
            'logged_in_user': traveller_user_logged_in,   #logged_in_user is for avatar in navbar
        }
    else:
        places = Place.objects.all()
        context = {
            'places':places,
        }
    return render(request, 'places/places.html', context) 


def placedetails(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    allow_review = True
    context_bool = False
    show_bool = True
    current_user=request.user
    if current_user.is_authenticated:
        traveller_user_logged_in= get_object_or_404(Traveller, email=current_user)
        notifications = Notification.objects.all().filter(receiver_email=current_user)

    if request.method == 'POST':
        if 'review_add' in request.POST:
            rating =  request.POST.get('rating')
            place_review = request.POST['preview']
            place_id = request.POST['plid']
            placeReviewed = get_object_or_404(Place, pk=place_id)
            Reviewer = traveller_user_logged_in
            if 'edit' in request.POST:
                reve_id = request.POST['edit']
               
                edit_review = get_object_or_404(Review, pk=reve_id)
                edit_review.place_review = place_review   
                edit_review.save()
            else:
                print(rating)
                re = Review(place_name=placeReviewed, Reviewer=Reviewer, place_review = place_review, ratings=rating)
                re.save()
        
        elif 'edit_rev' in request.POST:
            rev_id = request.POST['rev_id']
            edit_review = get_object_or_404(Review, pk=rev_id)
            context_bool = True
            show_bool = False
            print(edit_review)

        elif 'del_rev' in request.POST:
            rev_id = request.POST['rev_id']
            del_review = get_object_or_404(Review, pk=rev_id)
            del_review.delete()


       
    attractions= Major_Attraction.objects.all().filter(place=place)
    tasks= Things_To_Do.objects.all().filter(place=place)
    reviews = Review.objects.all().filter(place_name=place)
   
    temp_available_guides = Guide.objects.filter(places=place, is_active = True)
    available_guides=list()

    for i in temp_available_guides:
        user=i.email
        traveller=Traveller.objects.filter(email=user).first()

        available_guides.append({'guide':i , 'info':traveller})
    if current_user.is_authenticated:
        if Review.objects.all().filter(place_name=place, Reviewer=traveller_user_logged_in):
            allow_review = False
        context = {
            'available_guides' : available_guides,
            'place':place,
            'attractions':attractions,
            'tasks':tasks,
            'reviews':reviews,
            'notifications':notifications,
            'allow_review':allow_review,
            'show_bool':show_bool,
            'logged_in_user': traveller_user_logged_in,   #logged_in_user is for avatar in navbar
        }
        if context_bool:
            context.update({'edit_review':edit_review,
            })
    else:
        context = {
            'available_guides' : available_guides,
            'place':place,
            'attractions':attractions,
            'tasks':tasks,
            'reviews':reviews,
        }
    return render(request, 'places/placedetails.html', context) 

def search(request):
    if 'term' in request.GET:  #check for source files for autocomplete 
        pla = Place.objects.filter(name__icontains=request.GET.get('term'))
        placenames = list()         #create JSON list
        for place in pla:
            placenames.append(place.name)
        return JsonResponse(placenames, safe=False)
    searchtag = request.GET['search_places']
    places = Place.objects.all().filter(name__icontains=searchtag) | Place.objects.all().filter(keywords__search=searchtag) | Place.objects.all().filter(city__icontains=searchtag) | Place.objects.all().filter(country__icontains=searchtag )
    context = {
        'places':places
    }
    return render(request, 'places/places.html', context)
  



