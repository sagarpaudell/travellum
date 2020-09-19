from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from travellers.models import Traveller
from guides.models import Guide
from notifications.models import Notification
from history.models import History
from django.contrib import messages,auth
from datetime import datetime
import datetime
from django.utils.timezone import utc

def view_profile(request, traveller_id):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user_logged_in= get_object_or_404(Traveller, email=user)

    profile=get_object_or_404(Traveller, pk=traveller_id)
    if profile.email==user:
        return redirect('dashboard')

    elif user.is_authenticated:
        travel_history = History.objects.all().filter(traveller = user , guide = profile.email)
        has_travelled_with = False
        for history in travel_history:
            if history.tour_complete:
                has_travelled_with = True
        context = {
                'logged_in_user':traveller_user_logged_in,     #logged_in_user is for avatar in navbar
                'traveller_user':profile,
                'my_profile':False,
                'notifications': notifications,
                'has_travelled_with': has_travelled_with,
                 }
        return render(request, 'travellers/travellers.html',context)

    else:
        context = {
                'traveller_user':profile,
                'my_profile':False,
            }
        return render(request, 'travellers/tr9806800001avellers.html',context)




def notifications(request):
    if request.method == 'POST':
        sender_user = request.user
        traveller_id = request.POST['traveller_id']

        receiver = get_object_or_404(Traveller, pk=traveller_id)
        sender_name = sender_user.first_name+" " +sender_user.last_name
        receiver_user = get_object_or_404(User, email=receiver.email)
        reg_date = datetime.datetime.utcnow().replace(tzinfo=utc)

    #Check if user has made request already
    if request.user.is_authenticated:
        current_user = request.user
        has_requested = Notification.objects.all().filter(receiver_email=receiver_user, sender_email=sender_user )
        if has_requested:
            messages.error(request, 'You have already made a request to this guide')
            return redirect('/guides/'+traveller_id)
        else:
            notification = Notification(receiver_email=receiver_user, sender_email=sender_user, sender_name = sender_name, reg_date= reg_date)
            notification.save()
        return redirect('/guides/'+traveller_id)        
    return redirect('/guides/'+traveller_id)

def create_trip(request):
    return render(request, 'travellers/create_trip.html')


def payment_status(request):
    return render(request, 'travellers/payment_status.html')