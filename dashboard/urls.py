from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('confirm_trip/', views.confirm_trip, name="confirm_trip")

]
