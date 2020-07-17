from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegisterForm
from .email_authenticate import send_email,check_token


# Create your views here.

def register(request):
    #print(request.build_absolute_uri())
    
    """ if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #email = request.POST['email']
        if form.is_valid():
            form.save()
            #send_email(email,request)
            #password = form.cleaned_data.get('password')
            
            return redirect('login')
            
        else:
            # if (not form.clean_email):
            #     messages.warning(request, 'Email is taken')
            # if (not form.clean_password):
            #     messages.warning(request, "passwords don't match")
            return render(request, 'accounts/register.html' )
    """
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
        

@login_required
def profile(request):
    
        
    return render(request, "accounts/profile.html")
    #u_form = UserUpdateForm(request.POST,instance=request.user)
    #p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
    
    """ if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, f'your account has been updated!')
        """   
    
        
        
    """ else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html',context) """


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

def check_confirmation(request, slug):
    if check_token(slug):
        return redirect("profile")
    else:
        return HttpResponse('<h1> email not verified</h1>')
