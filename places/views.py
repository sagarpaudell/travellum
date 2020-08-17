from django.shortcuts import render,redirect

def places(request):
    return redirect('index')

def search(request):
    return render(request, 'places/search.html')
