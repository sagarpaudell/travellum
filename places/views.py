import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Place
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
    temp_available_guides = Guide.objects.filter(places=place)
    print(temp_available_guides)
    available_guides=list()

    for i in temp_available_guides:
        user=i.email
        traveller=Traveller.objects.filter(email=user).first()

        available_guides.append({'guide':i , 'info':traveller})
        print(user,traveller)
    context = {
        'available_guides' : available_guides,
        'place':place
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
  
