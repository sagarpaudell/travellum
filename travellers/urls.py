from django.urls import path
from . import views 

urlpatterns = [
    path('<int:traveller_id>', views.view_profile, name="view_profile"),
    path('create_trip/<int:traveller_id>', views.create_trip, name='create_trip'),
    path('', views.notifications, name="notifications"),
]