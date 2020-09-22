from django.utils import timezone
from django.http import HttpResponse
from travellers.models import Traveller
from places.models import Place
from guides.models import Guide
from accounts.models import User
from notifications.models import Notification, Trip_Notification
from django.shortcuts import render, redirect, get_object_or_404
 
def index(request):
    active_guides = Guide.objects.all().filter(is_active=True)
    x=list()
    context = dict()
    for guide in active_guides:
        traveller=Traveller.objects.filter(email=guide.email).first()
        time_indays = (timezone.now() - guide.email.last_login).seconds/86400
        if (time_indays<10):
            x.append(traveller)
            print(time_indays)
        else:
            guide.is_active = False
            print(f'{guide.email} hasn\'t logged in since {time_indays} days')
    places = Place.objects.all()[:6]
    context.update({
        'guides':x,
        'places':places
    })
    return render(request, 'pages/index.html', context)
def about(request):
    if request.user.is_authenticated:
        traveller_user = get_object_or_404(Traveller, email=request.user)
        notifications = Notification.objects.all().filter(receiver_email=request.user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user)
        if traveller_user.is_guide:
            guide_user1 = get_object_or_404(Guide, email=request.user)
            if guide_user1:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=request.user)
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user)

        context={
                'logged_in_user':traveller_user,
                'notifications': notifications,
                'trip_notifications': trip_notifications,
                }
        return render(request, 'pages/about.html',context)
    return render(request, 'pages/about.html')

