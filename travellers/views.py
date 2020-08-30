from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from travellers.models import Traveller

def view_profile(request, traveller_id):
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
                    }
            return render(request, 'dashboard/dashboard.html',context)
        else:
                traveller_user=Traveller.objects.all().filter(email=profile.email)
                context = {
                    'logged_in_user':traveller_user_logged_in,
                    'traveller_user':traveller_user,
                    'my_profile':False, 
                         }
                return render(request, 'dashboard/dashboard.html',context)

    else:
        traveller_user=Traveller.objects.all().filter(email=profile.email)
        context = {
                'traveller_user':traveller_user,
                'my_profile':False,
            }
        return render(request, 'dashboard/dashboard.html',context)