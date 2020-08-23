import json

from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import Place

def places(request):
    return render(request, 'places/places.html') 


def placedetails(request):
    return render(request, 'places/placedetails.html') 
<<<<<<< HEAD
    return redirect('index')
=======
>>>>>>> 501af96765ff5a25567ef51c184ab33685bb0d56

def search(request):
    if 'term' in request.GET:  #check for source files for autocomplete 
        pla = Place.objects.filter(name__icontains=request.GET.get('term'))
        placenames = list()         #create JSON list
        for place in pla:
            placenames.append(place.name)
        return JsonResponse(placenames, safe=False)
    return render(request, 'places/search.html')
