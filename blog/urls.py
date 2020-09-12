
from django.urls import path
from . import views

urlpatterns=[
    path('', views.my_blog, name='my_blog'),
    path('explore', views.explore, name='explore'),
    path('single_blog_post', views.single_blog_post, name='single_blog_post'),
]
