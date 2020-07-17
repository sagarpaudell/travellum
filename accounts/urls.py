
from django.urls import path

from django.contrib import admin

from . import views as account_views

urlpatterns = [
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view ,name='logout'),
    path('profile/', account_views.profile, name='profile'),
    path('profile/<path:slug>/', account_views.check_confirmation, name='slug'),
    path ('register/', account_views.register, name='register')
]
