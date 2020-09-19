from django.urls import path
from . import views 

urlpatterns = [
    path('<int:traveller_id>', views.view_profile, name="view_profile"),
    path('create_trip/', views.create_trip, name='create_trip'),
    path('payment_status/', views.payment_status, name='payment_status'),
    path('', views.notifications, name="notifications"),
]