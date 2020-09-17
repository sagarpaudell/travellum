
from django.urls import path

from django.contrib import admin

from . import views as account_views


urlpatterns = [
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view ,name='logout'),
    path('reset/', account_views.reset_view ,name='reset'),
    path('v_code/', account_views.v_code_view ,name='v_code'),
    path('change_pw/', account_views.change_pw_view ,name='change_pw'),
    
    
    path ('register/', account_views.register, name='register'),
]
