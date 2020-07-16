from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('register/', account_views.register, name='register'),
   
   
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pagee/index.html') ,name='logout'),
    path('profile/', account_views.profile, name='profile'),
    path('profile/<path:slug>/', account_views.check_confirmation, name='slug'),
    path ('register/', account_views.register, name='register')
]
