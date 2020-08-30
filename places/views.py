import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
<<<<<<< HEAD
from .models import Place, Major_Attraction, Things_To_Do
=======
from .models import Place, Review
>>>>>>> 2448c081ab35f0802eedb050c300954c317d8d6a
from guides.models import Guide
from travellers.models import Traveller

def places(request):
    places = Place.objects.all()
    context = {
        'places':places
    }
    return render(request, 'places/places.html', context) 


def placedetails(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
<<<<<<< HEAD
    attractions= Major_Attraction.objects.all().filter(place=place)
    tasks= Things_To_Do.objects.all().filter(place=place)
=======
    reviews = Review.objects.all().filter(place_name=place)
>>>>>>> 2448c081ab35f0802eedb050c300954c317d8d6a
    temp_available_guides = Guide.objects.filter(places=place)
    available_guides=list()

    for i in temp_available_guides:
        user=i.email
        traveller=Traveller.objects.filter(email=user).first()

        available_guides.append({'guide':i , 'info':traveller})
        print(user,traveller)
    context = {
        'available_guides' : available_guides,
        'place':place,
<<<<<<< HEAD
        'attractions':attractions,
        'tasks':tasks,
=======
        'reviews':reviews
>>>>>>> 2448c081ab35f0802eedb050c300954c317d8d6a
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
  
