from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .email_authenticate import send_email,check_token
from django.http import HttpResponse

# Create your views here.

def register(request):
    print(request.build_absolute_uri())
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST['email']
        if form.is_valid():
            form.save()
            send_email(email,request)
            #password = form.cleaned_data.get('password')
            messages.success(request, f'Hi, your account has been created! You can login now')
            return redirect('login')
            
        else:
            #messages.warning(request, 'fuck you enter valid info ')
            return render(request, 'accounts/register.html', )
    else:
        form = UserRegisterForm()
        print(request.user.pk)
        return render(request, 'accounts/register.html') #{'form':form} )
        

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


def login_view():
    pass
def check_confirmation(request, slug):
    if check_token(slug):
        return redirect("profile")
    else:
        return HttpResponse('<h1> email not verified</h1>')
