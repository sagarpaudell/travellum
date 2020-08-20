from django.shortcuts import render,redirect

def places(request):
    return render(request, 'places/places.html') 


def placedetails(request):
    return render(request, 'places/placedetails.html') 