from django.shortcuts import render
from places.models import Place
from travellers.models import Traveller
from .models import Blog, Comment


# Create your views here.
def my_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/myBlog.html', context={'blogs': blogs})


def explore(request):
    return render(request, 'blog/explore.html')
def single_blog_post(request):
    return render(request, 'blog/blogDetail.html')

