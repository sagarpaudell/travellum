import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Place

def places(request):
    places = Place.objects.all()
    context = {
        'places':places
    }
    return render(request, 'places/places.html', context) 


def placedetails(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    context = {
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
    places = Place.objects.all().filter(name__icontains=searchtag)
    context = {
        'places':places
    }
    return render(request, 'places/places.html', context)
  
