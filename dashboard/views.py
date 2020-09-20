from django.shortcuts import render,redirect, get_object_or_404
from accounts.models import User
from chat.models import Chat
from travellers.models import Traveller
from guides.views import GuideView, GuideUpdateView
from guides.models import Guide, Guide_Review
from guides.views import GuideView
from notifications.models import Notification, Trip_Notification
from places.models import Place
<<<<<<< HEAD
from places.models import Place
=======
from history.models import History
>>>>>>> 5a1762553b2f212bb12fc3851ecc1aad24d46e42
from datetime import datetime, timedelta
from django import template
import datetime
from django.utils.timesince import timesince
from django.utils.timezone import utc

# Create your views here.
def dashboard(request):
  user=request.user
  traveller_user=get_object_or_404(Traveller, email=user)
  bio = traveller_user.bio.split('.',5)
  bio_first = ". ".join(bio[:5])+(".")
  guide_user = Guide.objects.all().filter(email=user).first()
  guide_reviews = Guide_Review.objects.all().filter(guide=user)
  notifications = Notification.objects.all().filter(receiver_email=user)
<<<<<<< HEAD
=======
  trip_notifications = Trip_Notification.objects.all().filter(receiver_email=user)
>>>>>>> 5a1762553b2f212bb12fc3851ecc1aad24d46e42
  places = Place.objects.all()
  place_pattern=''
  for place in places:
      place_pattern = place.name+'|'+place_pattern
  
  
  context = {
                'traveller_user':traveller_user,
                'my_profile':True,
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'guide_user' : guide_user,
                'notifications': notifications,
                'trip_notifications': trip_notifications,
                'bio_first': bio_first,
                'places' : places,
                'place_pattern' : place_pattern,
                'guide_reviews': guide_reviews,
            }
  

  if (len(bio)>=5):
    bio_second = bio[5]
    context = {
                'traveller_user':traveller_user,
                'my_profile':True,
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'guide_user' : guide_user,
                'notifications': notifications,
                'trip_notifications': trip_notifications,
                'bio_first': bio_first,
                'bio_second': bio_second,
                'guide_reviews': guide_reviews,
            }
 
  if (request.method == "POST" ):
    root_user = get_object_or_404(User, email=user)
    traveller_user = get_object_or_404(Traveller, email=user)
    
    if 'Update Profile' in request.POST:
      
      traveller_user.first_name = request.POST['first_name'].title()
      traveller_user.last_name = request.POST['last_name'].title()
      traveller_user.address = request.POST['address'].title()
      traveller_user.slogan = request.POST['slogan']
      traveller_user.bio = request.POST['bio']
      traveller_user.languages = request.POST['languages']
      traveller_user.gender = request.POST['gender']
        
      if request.FILES:
        traveller_user.photo_main = request.FILES['photo_main']
      
      traveller_user.save()

      root_user.first_name = request.POST['first_name'].title()
      root_user.last_name = request.POST['last_name'].title()
      print(traveller_user.photo_main)
      root_user.save()
      return redirect ('dashboard')
      
      #for guide creation form
    if 'Guide-Form' in request.POST:
      GuideView(request)  #calls guide's view in guide app

    if 'Guide-Update-Form' in request.POST:
      GuideUpdateView(request)
    

    
    #for notification
    # if 'request_guide' in request.POST:
    #   notifications(request) 
      
    # return redirect('dashboard')
  
 
    if 'accepted' in request.POST:
      receiver_email = request.POST['receiver_email']
      receiver_user = get_object_or_404(User,email=receiver_email)
      sender_user = request.user
      sender_name = sender_user.first_name+" " +sender_user.last_name
      reg_date = datetime.datetime.utcnow().replace(tzinfo=utc)
      noti_id = request.POST['noti_id']
      noti = get_object_or_404(Notification, pk=noti_id)
      noti.completed = True
      noti.save()
      notification = Notification(receiver_email=receiver_user, sender_email=sender_user, sender_name = sender_name,is_accepted = True, reg_date= reg_date)
      notification.save()
      chat = Chat(sender = receiver_user, receiver = sender_user, message_text = 'hello')
      chat.save()

    if 'ignored' in request.POST:
      noti_id = request.POST['noti_id']
      receiver_email = request.POST['receiver_email']
      receiver_user = get_object_or_404(User,email=receiver_email)
      sender_user = request.user
      sender_name = sender_user.first_name+" " +sender_user.last_name
      reg_date = datetime.datetime.utcnow().replace(tzinfo=utc)
      noti_id = request.POST['noti_id']
      noti = get_object_or_404(Notification, pk=noti_id)
      noti.completed = True
      noti.save()
      notification = Notification(receiver_email=receiver_user, sender_email=sender_user, sender_name = sender_name,is_ignored = True, reg_date= reg_date)
      notification.save()

  return render(request, 'dashboard/dashboard.html',context)

def confirm_trip(request):
  traveller_user = get_object_or_404 (Traveller , email=request.user)
  if request.method == "POST":
    trip_noti_id = request.POST['tn_id']
    tn_instance = get_object_or_404(Trip_Notification,pk=trip_noti_id)
  context = {
                'traveller_user':traveller_user,
                'logged_in_user':traveller_user,
                'tn_instance':tn_instance, 
            }
  return render(request, 'dashboard/confirm_trip.html',context)

  
    





