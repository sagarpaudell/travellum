from django.shortcuts import render
from django.http import HttpResponse
from travellers.models import Traveller
from places.models import Place
from guides.models import Guide
 
def index(request):

    published_guides = Guide.objects.all().filter(is_published=True)
    x=list()
    for guide in published_guides:
        traveller=Traveller.objects.filter(email=guide.email).first()
        x.append(traveller)
        
    places = Place.objects.all()[:6]
    context = {
        'guides':x,
        'places':places
    }
    return render(request, 'pages/index.html', context)
def login(request):
    return render(request, 'pages/login.html')
def register(request):
    return render(request, 'pages/register.html')
