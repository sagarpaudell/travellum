from django.shortcuts import render
from accounts.models import User
from travellers.models import Traveller

# Create your views here.
def dashboard(request):
  user=request.user
  traveller_user=Traveller.objects.all().filter(email=user)
  context = {
              'traveller_user':traveller_user,
            }
  return render(request, 'dashboard/dashboard.html',context)

