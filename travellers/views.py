from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return render(request,'travellers.html')
    return HttpResponse('<h1>Travellers</h1>')