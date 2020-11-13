from django.shortcuts import render

posts = [
    {
        'author' : 'Flavien Chamay',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : '11/11/2020'
    },
    {
        'author' : 'Romain Chamay',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : '12/11/2020'
    }
]

def homePage(request):
    context = {
        'posts' : posts
    }
    
    return render(request, 'blog/home.html', context)

def aboutPage(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

