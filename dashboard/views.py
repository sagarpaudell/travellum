from django.shortcuts import render,redirect
from accounts.models import User
from travellers.models import Traveller

# Create your views here.
def dashboard(request):
  user=request.user
  traveller_user=Traveller.objects.all().filter(email=user)
  for traveller in traveller_user:
    traveller_dp=traveller.photo_main
  context = {
                'traveller_user':traveller_user,
                'my_profile':True,
                'traveller_dp':traveller_dp,
            }
  
  if (request.method == 'POST' ):
    root_user = User.objects.all().filter(email=user)
    traveller_user = Traveller.objects.all().filter(email=user)
    if 'Update Profile' in request.POST:
      for traveller in traveller_user:
        traveller.first_name = request.POST['first_name'].title()
        traveller.last_name = request.POST['last_name'].title()
        traveller.address = request.POST['address'].title()
        traveller.slogan = request.POST['slogan']
        traveller.bio = request.POST['bio']
        traveller.languages = request.POST['languages']
        if traveller.is_guide:
          traveller.price_per_hour = request.POST['pph']
        traveller.gender = request.POST['gender']
        
        if request.FILES:
          traveller.photo_main = request.FILES['photo_main']
      
        traveller.save()

      for user in root_user:
        user.first_name = request.POST['first_name'].title()
        user.last_name = request.POST['last_name'].title()
        user.save()
    return redirect('dashboard')

  return render(request, 'dashboard/dashboard.html',context)  





  

