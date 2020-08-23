from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegisterForm
from travellers.models import Traveller



# Create your views here.

def register(request):
    #print(request.build_absolute_uri())
 
    if (request.method == "POST"):
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
            
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'That email is being used')
            return redirect('register')
        else:
            user = User.objects.create_user(
                email = email,
                first_name = first_name,
                last_name =last_name,
                
                password = password1
            )
            user.set_password(password1)
            user.save()
            traveller=Traveller(first_name=first_name,last_name=last_name,email=User.objects.get(email = email))
            traveller.save()
            return redirect('login')

    else:
        #print(request.user.email)
        return render(request, 'accounts/register.html') 
        
def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_authenticated:
                return redirect('dashboard')
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('index')


