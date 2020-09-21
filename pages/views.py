from django.utils import timezone
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
        time_indays = (timezone.now() - guide.email.last_login).seconds/86400
        if (time_indays<0.5):
            x.append(traveller)
            print(time_indays)
        else:
            print(f'{guide.email} hasn\'t logged in since {time_indays} days')
    places = Place.objects.all()[:6]
    context = {
        'guides':x,
        'places':places
    }
    return render(request, 'pages/index.html', context)
def about(request):
    return render(request, 'pages/about.html')
