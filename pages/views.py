from django.shortcuts import render
from django.http import HttpResponse
from travellers.models import Traveller
 
def index(request):
    guides = Traveller.objects.all().filter(is_guide=True)
    context = {
        'guides':guides
    }
    return render(request, 'pages/index.html', context)
def login(request):
    return render(request, 'pages/login.html')
def register(request):
    return render(request, 'pages/register.html')
