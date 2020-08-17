from django.urls import path
from . import views


urlpatterns = [
    path('', views.places, name="places"),
     path('search', views.search, name="search")
]