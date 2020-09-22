from django.utils import timezone
from django.http import HttpResponse
from travellers.models import Traveller
from places.models import Place
from guides.models import Guide
from accounts.models import User
from notifications.models import Notification, Trip_Notification
from django.shortcuts import render, redirect, get_object_or_404
 
def index(request):
    active_guides = Guide.objects.all().filter(is_active=True).order_by('-average_rating')[:4]
    x=list()
    context = dict()
    for guide in active_guides:
        traveller=Traveller.objects.filter(email=guide.email).first()
        time_indays = (timezone.now() - guide.email.last_login).seconds/86400
        if (time_indays<10):
            x.append(guide)
            print(time_indays)
        else:
            guide.is_active = False
            print(f'{guide.email} hasn\'t logged in since {time_indays} days')
    places = Place.objects.all()[:6]
    context.update({
        'guides':x,
        'places':places,
    })
    return render(request, 'pages/index.html', context)
def about(request):
    if request.user.is_authenticated:
        traveller_user = get_object_or_404(Traveller, email=request.user)
        notifications = Notification.objects.all().filter(receiver_email=request.user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        if traveller_user.is_guide:
            guide_user1 = get_object_or_404(Guide, email=request.user)
            if guide_user1:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=request.user).order_by('-noti_date')
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')

        
    if notifications:
        new_noti = notifications.last().reg_date
        if notifications.count()>1:
            last_noti = notifications[1].reg_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
    if trip_notifications:
        new_tnoti = trip_notifications.last().noti_date
        if trip_notifications.count()>1:
            last_noti = trip_notifications[1].noti_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
        elif trip_notifications.count()==1:
            messages.info(request, 'You have new notifications.')

        context={
                'logged_in_user':traveller_user,
                'notifications': notifications,
                'trip_notifications': trip_notifications,
                }
        return render(request, 'pages/about.html',context)
    return render(request, 'pages/about.html')

