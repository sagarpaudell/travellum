from django.shortcuts import render
from places.models import Place
from travellers.models import Traveller
from guides.models import Guide
from .models import Blog, Comment


# Create your views here.
def my_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/myBlog.html', context={'blogs': blogs})


def explore(request):
    return render(request, 'blog/explore.html')
def single_blog_post(request):
    return render(request, 'blog/blogDetail.html')
def create_blog_post(request):
    
    print(request.POST)
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

    

    return render(request, 'blog/createPost.html',{'places':places, 'place_pattern':place_pattern[:-1]})


