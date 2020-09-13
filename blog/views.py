from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from travellers.models import Traveller
from notifications.models import Notification


def my_blog(request):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user = get_object_or_404(Traveller, email=user)
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
            }
    return render(request, 'blog/myBlog.html',context)


def explore(request):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user = get_object_or_404(Traveller, email=user)
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
            }
    return render(request, 'blog/explore.html',context)


def single_blog_post(request):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user = get_object_or_404(Traveller, email=user)
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
            }
    return render(request, 'blog/blogDetail.html',context)


def create_blog_post(request):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user = get_object_or_404(Traveller, email=user)
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
            }
    return render(request, 'blog/createPost.html',context)

