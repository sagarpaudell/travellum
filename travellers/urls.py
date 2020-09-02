from django.urls import path
from . import views 

urlpatterns = [
    path('<int:traveller_id>', views.view_profile, name="view_profile"),
    path('', views.notifications, name="notifications"),
]