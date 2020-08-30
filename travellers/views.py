from django.shortcuts import render,redirect
from accounts.models import User
from travellers.models import Traveller
from guides.models import Guide, GuideReview

def view_profile(request, traveller_id):
  user=request.user
  
  if "review_form" in request.POST:
    print(request.POST)
   
    review_detail=request.POST
    review_text= review_detail['review']
    review_rating= review_detail['rating']
    
    guide_email=Traveller.objects.get(id=traveller_id).email
    reviewer=Traveller.objects.get(email=request.user)
    guide = Guide.objects.get(email=guide_email)
    review = GuideReview(reviewer=reviewer, guide=guide, review_score=review_rating, review_text=review_text)
    review.save()

  if user.is_authenticated:
    traveller_user_logged_in=Traveller.objects.all().filter(email=user)
    for traveller in traveller_user_logged_in:
        traveller_dp=traveller.photo_main

  profile=Traveller.objects.all().filter(id=traveller_id)
  for profile in profile:
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

  
    
