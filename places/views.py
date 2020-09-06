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
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=current_user)
        places = Place.objects.all()
        context = {
            'places':places,
            'notifications': notifications,
        }
    else:
        places = Place.objects.all()
        context = {
            'places':places,
        }
    return render(request, 'places/places.html', context) 


def placedetails(request, place_id):
    current_user=request.user
    if current_user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=current_user)
    place = get_object_or_404(Place, pk=place_id)
    attractions= Major_Attraction.objects.all().filter(place=place)
    tasks= Things_To_Do.objects.all().filter(place=place)
    reviews = Review.objects.all().filter(place_name=place)
    temp_available_guides = Guide.objects.filter(places=place)
    available_guides=list()

    for i in temp_available_guides:
        user=i.email
        traveller=Traveller.objects.filter(email=user).first()

        available_guides.append({'guide':i , 'info':traveller})
        print(user,traveller)
    if current_user.is_authenticated:
        context = {
            'available_guides' : available_guides,
            'place':place,
            'attractions':attractions,
            'tasks':tasks,
            'reviews':reviews,
            'notifications': notifications,
        }
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
    places = Place.objects.all().filter(name__icontains=searchtag) | Place.objects.all().filter(description__icontains=searchtag) | Place.objects.all().filter(city__icontains=searchtag) | Place.objects.all().filter(country__icontains=searchtag )
    context = {
        'places':places
    }
    return render(request, 'places/places.html', context)
  