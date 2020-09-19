from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib import messages,auth
from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegisterForm
from travellers.models import Traveller
from django.conf import settings


# Create your views here.

def register(request):
    if (request.method == "POST"):
        
        first_name = request.POST['first_name'].title()
        last_name = request.POST['last_name'].title()
        email = request.POST['email']
        password1 = request.POST['password1']
            
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'The email is being used')
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
            send_verificationmail(email)            
            messages.info(request, 'verification link has been sent to your account')
            return redirect('login')

    else:
        return render(request, 'accounts/register.html') 
        

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            traveller = Traveller.objects.get(email=user)
            if traveller.is_published:
                auth.login(request, user)
                if user.is_authenticated:
                    return redirect('dashboard')
            else:
                messages.warning(request, 'verification link has been sent to your account. You need to verify your account 1st to login')
                return redirect('login')
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')



def logout_view(request):
    auth.logout(request)
    return redirect('index')


def reset_view(request):
    """password reset view here the user gives the username for which the password is to be reset"""
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email = email)
        if user.exists() :
            token = default_token_generator.make_token(user.first())
            subject = f'password reset'
            message = f'follow this link to reset your password\
                http://127.0.0.1:8000/accounts/change_pw/{email}/{token}/'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list)
            messages.info(request, 'password reset link has been sent to your accounts')
    return render(request, 'accounts/reset.html')


def v_code_view(request, email=None, token=None):
    """this function runs when the user clicks the password reset link"""
    user = User.objects.filter(email = email)
    print(request, email)
    if request.method == 'POST':
        if email in request.POST:
            user = user.first()
            password = request.POST['new_pw1']
            user.set_password(password)
            user.save()
            print('hello')
            messages.success(request,'your password has been successfully reset. Now you can login')
        
    else:
        if user.exists():
            link_verified = default_token_generator.check_token(user.first(), token)
            print(link_verified)
            if link_verified:
                messages.success(request,'the link was verified now you can reset your email')
                return render(request, 'accounts/change.html', {'email':email})
            else:
                messages.warning(request,'the password reset link you clicked wasn\'t sent from us')
                return redirect('login')

        else:
            messages.warning('the email doesn\'t exist in our databse')
            return redirect('login')
    return redirect('login')

   


def change_pw_view(request):
    return render(request, 'accounts/change.html')



def send_verificationmail(email):
    """ sends verification mail"""
    user =  User.objects.get(email = email)
    token = default_token_generator.make_token(user)
    subject = f'email verification link'
    message = f'follow this link to verify your account\
        http://127.0.0.1:8000/accounts/verify_mail/{user.email}/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )    


def verify_mail(request, email, token):
    """checks if the token in the link matches the user"""
    user = User.objects.get(email=email)
    email_verified = default_token_generator.check_token(user, token)
    if email_verified:
        traveller = Traveller.objects.get(email=user)
        traveller.is_published = True
        traveller.save()
        messages.success(request, 'email verified now you can login')
        return redirect('login')
    else:
        messages.error(request, 'the verification link was fake or it expired')
        return redirect('login')