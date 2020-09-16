from django.shortcuts import render,redirect, get_object_or_404
from accounts.models import User
from travellers.models import Traveller
from guides.models import Guide
from guides.views import GuideView
from notifications.models import Notification
from places.models import Place

# Create your views here.
def dashboard(request):
  user=request.user
  traveller_user=get_object_or_404(Traveller, email=user)
  guide_user = Guide.objects.all().filter(email=user).first()
  notifications = Notification.objects.all().filter(receiver_email=user)
  context = {
                'traveller_user':traveller_user,
                'my_profile':True,
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'guide_user' : guide_user,
                'notifications': notifications,
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
      if traveller_user.is_guide:
        traveller_user.price_per_hour = request.POST['pph']
      traveller_user.gender = request.POST['gender']
        
      if request.FILES:
        traveller_user.photo_main = request.FILES['photo_main']
      
      traveller_user.save()

      root_user.first_name = request.POST['first_name'].title()
      root_user.last_name = request.POST['last_name'].title()
      root_user.save()
      
      #for guide form
    if 'Guide-Form' in request.POST:
      GuideView(request)  #calls guide's view in guide app
    
    #for notification
    if 'request_guide' in request.POST:
      notifications(request) 
      
    return redirect('dashboard')
  return render(request, 'dashboard/dashboard.html',context)

  
    





