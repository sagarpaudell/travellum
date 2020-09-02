from django.shortcuts import render, redirect
from .models import Notification

def notifications(request):
    return render(request, 'dashboard/dashboard.html')
