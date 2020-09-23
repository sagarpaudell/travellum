from places.models import Place
from travellers.models import Traveller
from guides.models import Guide
from notifications.models import Notification, Trip_Notification
from .models import Blog, Comment
from urllib.parse import urlparse
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def my_blog(request):
    user=request.user
    if user.is_authenticated:
        traveller_user = get_object_or_404(Traveller, email=user)
        notifications = Notification.objects.all().filter(receiver_email=request.user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        if traveller_user.is_guide:
            guide_user1 = get_object_or_404(Guide, email=request.user)
            if guide_user1:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=request.user).order_by('-noti_date')
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        
    if notifications:
        new_noti = notifications.last().reg_date
        if notifications.count()>1:
            last_noti = notifications[1].reg_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
    if trip_notifications:
        new_tnoti = trip_notifications.last().noti_date
        if trip_notifications.count()>1:
            last_noti = trip_notifications[1].noti_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
        elif trip_notifications.count()==1:
            messages.info(request, 'You have new notifications.')

        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
                'trip_notifications':trip_notifications,
            }
    blogs = request.user.blogs.all()
    context.update({'blogs': blogs})
    return render(request, 'blog/myBlog.html', context)


def explore(request):
    user=request.user
    context = dict()
    if user.is_authenticated:
        traveller_user = get_object_or_404(Traveller, email=user)
        notifications = Notification.objects.all().filter(receiver_email=request.user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        if traveller_user.is_guide:
            guide_user1 = get_object_or_404(Guide, email=request.user)
            if guide_user1:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=request.user).order_by('-noti_date')
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
    
    if notifications:
        new_noti = notifications.last().reg_date
        if notifications.count()>1:
            last_noti = notifications[1].reg_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
    if trip_notifications:
        new_tnoti = trip_notifications.last().noti_date
        if trip_notifications.count()>1:
            last_noti = trip_notifications[1].noti_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
        elif trip_notifications.count()==1:
            messages.info(request, 'You have new notifications.')

        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
                'trip_notifications': trip_notifications,
            }
    
    places = Place.objects.all()
    context.update({'places': places})
    return render(request, 'blog/explore.html', context)




def single_blog_post(request,id):
    user=request.user
    context = dict()
    if user.is_authenticated:
        traveller_user = get_object_or_404(Traveller, email=user)
        notifications = Notification.objects.all().filter(receiver_email=request.user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        if traveller_user.is_guide:
            guide_user1 = get_object_or_404(Guide, email=request.user)
            if guide_user1:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=request.user).order_by('-noti_date')
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
    
    if notifications:
        new_noti = notifications.last().reg_date
        if notifications.count()>1:
            last_noti = notifications[1].reg_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
    if trip_notifications:
        new_tnoti = trip_notifications.last().noti_date
        if trip_notifications.count()>1:
            last_noti = trip_notifications[1].noti_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
        elif trip_notifications.count()==1:
            messages.info(request, 'You have new notifications.')

        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
                'trip_notifications':trip_notifications,
            }
    
    blog = Blog.objects.get(id=id)
    comments = blog.comments.all().order_by('-comment_time')
    # user_picture = Traveller.objects.get(email=request.user).photo_main 
    guide = Guide.objects.filter(email = blog.user).first()
    print(guide)
    is_guide = False if not guide else guide.is_published
    context.update({
        'blog':blog,
        'is_guide': is_guide,
        'comments':comments,
        # 'user_picture':user_picture,
    })
    
    if request.method=='POST':
        comment_text = request.POST['comment']
        comment=Comment(blog_id=blog, user=request.user, comment=comment_text)
        comment.save()

    return render(request, 'blog/blogDetail.html', context)


@login_required
def create_blog_post(request):
    user=request.user
    if user.is_authenticated:
        traveller_user = get_object_or_404(Traveller, email=user)
        notifications = Notification.objects.all().filter(receiver_email=request.user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        if traveller_user.is_guide:
            guide_user1 = get_object_or_404(Guide, email=request.user)
            if guide_user1:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=request.user).order_by('-noti_date')
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
    if notifications:
        new_noti = notifications.last().reg_date
        if notifications.count()>1:
            last_noti = notifications[1].reg_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
    if trip_notifications:
        new_tnoti = trip_notifications.last().noti_date
        if trip_notifications.count()>1:
            last_noti = trip_notifications[1].noti_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
        elif trip_notifications.count()==1:
            messages.info(request, 'You have new notifications.')
        
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
                'trip_notifications':trip_notifications,
            }
    
    if request.method == 'POST':
        form_data = request.POST
        title = form_data['title']
        description = form_data['description']
        photo = request.FILES['photo']
        place= request.POST['place']
        guide = Guide.objects.filter(email = request.user).first()
        is_guide = False if not guide else guide.is_published
        blog = Blog(
            user        = request.user, 
            title       = title, 
            description = description,
            photo       = photo,
            place       = Place.objects.get(name=place),
            is_guide    = is_guide
        )
        blog.save()
        messages.success(request, 'Blog created')
        return redirect('my_blog')
    places=Place.objects.all()
    place_pattern=''
    for place in places:
        place_pattern = place.name+'|'+place_pattern
    context.update({
        'places':places,
         'place_pattern':place_pattern[:-1],
         'logged_in_user':traveller_user, 
    })

    return render(request, 'blog/createPost.html',context)

@login_required
def edit_blog_post(request, blog_id):
    user=request.user
    if user.is_authenticated:
        traveller_user = get_object_or_404(Traveller, email=user)
        notifications = Notification.objects.all().filter(receiver_email=request.user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        if traveller_user.is_guide:
            guide_user1 = get_object_or_404(Guide, email=request.user)
            if guide_user1:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=request.user).order_by('-noti_date')
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        
    if notifications:
        new_noti = notifications.last().reg_date
        if notifications.count()>1:
            last_noti = notifications[1].reg_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
    if trip_notifications:
        new_tnoti = trip_notifications.last().noti_date
        if trip_notifications.count()>1:
            last_noti = trip_notifications[1].noti_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
        elif trip_notifications.count()==1:
            messages.info(request, 'You have new notifications.')        
        
        context = {
                'logged_in_user':traveller_user,   #logged_in_user is for avatar in navbar
                'notifications': notifications,
                'trip_notifications':trip_notifications,
            }

    if request.method == 'POST':
        form_data = request.POST
        title = form_data['title']
        description = form_data['description']
        place= request.POST['place']
        guide = Guide.objects.filter(email = request.user).first()
        is_guide = False if not guide else guide.is_published
        blog = get_object_or_404(Blog, pk=blog_id)
        print(form_data)
        blog.title       = title 
        blog.description = description
        
        if 'photo' in request.FILES:
            blog.photo       = request.FILES['photo']
        blog.place       = Place.objects.get(name=place)
        blog.is_guide    = is_guide
        blog.save()
        
        return redirect('single_blog_post', id=blog_id)

    places=Place.objects.all()
    place_pattern=''
    for place in places:
        place_pattern = place.name+'|'+place_pattern
    blog = get_object_or_404(Blog, pk=blog_id)
    context.update({
        'blog': blog,
        'places':places,
        'place_pattern':place_pattern[:-1],
        'logged_in_user':traveller_user, 
    })
    return render(request, 'blog/editPost.html', context)


@login_required
def delete_blog_post(request, blog_id):
    blog = get_object_or_404(Blog, id = blog_id)
    if request.user == blog.user:
        blog.delete()
    messages.success('Your blog was deleted')
    return redirect('my_blog')

def blogs_byplace(request, id):
    place = Place.objects.get(pk= id)
    print(place)
    blogs = Blog.objects.filter(place = place)
    print(blogs)
    return render(request, 'blog/place_blog.html', {'blogs':blogs, 'place':place})

def blogs_byuser(request, id):
    user = Traveller.objects.get(id = id).email
    blogs = user.blogs.all()
    print(blogs)
    
    if request.user.is_authenticated:
        traveller_user = get_object_or_404(Traveller, email=request.user)
        notifications = Notification.objects.all().filter(receiver_email=request.user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        if traveller_user.is_guide:
            guide_user1 = get_object_or_404(Guide, email=request.user)
            if guide_user1:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=request.user).order_by('-noti_date')
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=request.user).order_by('-noti_date')
        
    if notifications:
        new_noti = notifications.last().reg_date
        if notifications.count()>1:
            last_noti = notifications[1].reg_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
    if trip_notifications:
        new_tnoti = trip_notifications.last().noti_date
        if trip_notifications.count()>1:
            last_noti = trip_notifications[1].noti_date
            new_noti_check = (last_noti<new_noti)
            if (new_noti_check):
                messages.info(request, 'You have new notifications.')
            else:
                messages.info(request, 'You have no new notifications')
        elif trip_notifications.count()==1:
            messages.info(request, 'You have new notifications.')        
        
        context={
                'blogs':blogs,
                'logged_in_user':traveller_user,
                'notifications': notifications,
                'trip_notifications':trip_notifications,

                    }
        return render(request, 'blog/place_blog.html', context)
    return render(request, 'blog/place_blog.html')

