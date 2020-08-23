from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('<int:traveller_id>', views.view_profile, name="view_profile"),
]
