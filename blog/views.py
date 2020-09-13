from django.shortcuts import render, redirect, get_object_or_404
from places.models import Place
from travellers.models import Traveller
from guides.models import Guide
from notifications.models import Notification
from .models import Blog, Comment



# Create your views here.
def my_blog(request):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user = get_object_or_404(Traveller, email=user)
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
            }
    blogs = Blog.objects.filter(user=request.user)
    context.update({'blogs': blogs})
    return render(request, 'blog/myBlog.html', context)


def explore(request):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user = get_object_or_404(Traveller, email=user)
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
            }
    blogs = Blog.objects.filter(user=request.user)
    context.update({'blogs': blogs})
    return render(request, 'blog/explore.html', context)

def single_blog_post(request,id):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user = get_object_or_404(Traveller, email=user)
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
            }
    
    
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog_id=id)
    user_picture = Traveller.objects.get(email=request.user).photo_main 
    
    context.update({
        'blog':blog,
        'comments':comments,
        'user_picture':user_picture
    })
    
    if request.method=='POST':
        comment_text = request.POST['comment']
        comment=Comment(blog_id=blog, user=request.user, comment=comment_text)
        comment.save()

    return render(request, 'blog/blogDetail.html', context)

def create_blog_post(request):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user = get_object_or_404(Traveller, email=user)
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
            }
    
    if request.method == 'POST':
        form_data = request.POST
        title = form_data['title']
        description = form_data['description']
        photo = request.FILES['photo']
        place= request.POST['place']
        blog = Blog(
            user        = request.user, 
            title       = title, 
            description = description,
            photo       = photo,
            place       = Place.objects.get(name=place),
            is_guide    = Guide.objects.get(email=request.user).is_published,
        )
        blog.save()
    places=Place.objects.all()
    place_pattern=''
    for place in places:
        place_pattern = place.name+'|'+place_pattern
    context.update({
        'places':places,
         'place_pattern':place_pattern[:-1]
    })

    return render(request, 'blog/createPost.html',context)


