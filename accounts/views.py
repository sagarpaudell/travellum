from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegisterForm



# Create your views here.

def register(request):
    #print(request.build_absolute_uri())
 
    if (request.method == "POST"):
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
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
                return redirect('login')
        else:
            messages.error(request, "Passwords doesn't match")
            return redirect('register')
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
            return redirect('index')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('index')


