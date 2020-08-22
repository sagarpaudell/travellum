import json

from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import Place

def places(request):
    return redirect('index')

def search(request):
    if 'term' in request.GET:  #check for source files for autocomplete 
        pla = Place.objects.filter(name__icontains=request.GET.get('term'))
        placenames = list()         #create JSON list
        for place in pla:
            placenames.append(place.name)
        return JsonResponse(placenames, safe=False)
    return render(request, 'places/search.html')
