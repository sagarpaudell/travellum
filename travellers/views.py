from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from travellers.models import Traveller
from guides.models import Guide
from notifications.models import Notification
from django.contrib import messages,auth

def view_profile(request, traveller_id):
  user=request.user
  notifications = Notification.objects.all().filter(receiver_email=user)
  

  if user.is_authenticated:
    traveller_user_logged_in=Traveller.objects.all().filter(email=user)
    for traveller in traveller_user_logged_in:
        traveller_dp=traveller.photo_main
    user=request.user
    if user.is_authenticated:
        traveller_user_logged_in=Traveller.objects.all().filter(email=user)
        for traveller in traveller_user_logged_in:
            traveller_dp=traveller.photo_main

    profile=get_object_or_404(Traveller, pk=traveller_id)
    if profile.email==user:
        return redirect('dashboard')

    elif user.is_authenticated:
        if traveller_dp:
            traveller_user=Traveller.objects.all().filter(email=profile.email)
            context = {
                    'traveller_user':traveller_user,
                    'my_profile':False,
                    'traveller_dp':traveller_dp,
                    'notifications': notifications,
                    }
            return render(request, 'dashboard/dashboard.html',context)
        else:
                traveller_user=Traveller.objects.all().filter(email=profile.email)
                context = {
                    'logged_in_user':traveller_user_logged_in,
                    'traveller_user':traveller_user,
                    'my_profile':False,
                    'notifications': notifications, 
                         }
                return render(request, 'dashboard/dashboard.html',context)

    else:
        traveller_user=Traveller.objects.all().filter(email=profile.email)
        context = {
                'traveller_user':traveller_user,
                'my_profile':False,
            }
        return render(request, 'dashboard/dashboard.html',context)




def notifications(request):
    if request.method == 'POST':
        sender_user = request.user
        traveller_id = request.POST['traveller_id']
        receiver = get_object_or_404(Traveller, pk=traveller_id)
        sender_name = sender_user.first_name+" " +sender_user.last_name
        receiver_user = get_object_or_404(User, email=receiver.email)

    #Check if user has made request already
    if request.user.is_authenticated:
        current_user = request.user
        has_requested = Notification.objects.all().filter(receiver_email=receiver_user, sender_email=sender_user )
        if has_requested:
            messages.error(request, 'You have already made a request to this guide')
            return redirect('/guides/'+traveller_id)
        else:
            notification = Notification(receiver_email=receiver_user, sender_email=sender_user, sender_name = sender_name)
            notification.save()
        return redirect('/guides/'+traveller_id)        
    return redirect('/guides/'+traveller_id)