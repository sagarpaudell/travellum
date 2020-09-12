from django.shortcuts import render

# Create your views here.
def my_blog(request):
    return render(request, 'blog/myBlog.html')
def explore(request):
    return render(request, 'blog/explore.html')
def single_blog_post(request):
    return render(request, 'blog/blogDetail.html')
def create_blog_post(request):
    return render(request, 'blog/createPost.html')

