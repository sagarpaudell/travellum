from django.urls import path
from . import views


urlpatterns = [
    path('', views.places, name="places"),
    path('<int:place_id>', views.placedetails, name="placedetails"),
    path('search', views.search, name="search")
]