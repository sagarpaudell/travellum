
from django.urls import path
from . import views

urlpatterns=[
    path('', views.my_blog, name='my_blog'),
    path('explore/', views.explore, name='explore'),
    path('blogs_byplace/<int:id>', views.blogs_byplace, name='blogs_byplace'),
    path('single_blog_post/<int:id>', views.single_blog_post, name='single_blog_post'),
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('edit_blog_post/<int:blog_id>', views.edit_blog_post, name='edit_blog_post'),
    path('delete_blog_post/<int:blog_id>', views.delete_blog_post, name='delete_blog_post')
]
