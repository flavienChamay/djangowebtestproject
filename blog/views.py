from django.shortcuts import render
#To use our queries instead of dummy datas:
from .models import Post


def homePage(request):
    context = {
        #import our data from the Query 
        'posts' : Post.objects.all()
    }
    
    return render(request, 'blog/home.html', context)

def aboutPage(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

