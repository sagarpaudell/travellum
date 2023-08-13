from django.urls import path
from . import views as account_views


urlpatterns = [
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),
    path('register/', account_views.register, name='register'),
    path('reset/', account_views.reset_view, name='reset'),
    path('verify_mail/<str:email>/<str:token>/', account_views.verify_mail),
    path('change_pw/<str:email>/<str:token>/', account_views.v_code_view, name='v_code'),
    path('v_code/', account_views.change_pw_view, name='change_pw'),
]
