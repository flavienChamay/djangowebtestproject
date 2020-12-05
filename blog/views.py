from django.shortcuts import render
#To use our queries instead of dummy datas:
from .models import Post
#To prevent from creating a new post without login in
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView, #Being able to update information of posts in the frontend of the site
    DeleteView
)


def homePage(request):
    context = {
        #import our data from the Query 
        'posts' : Post.objects.all()
    }
    
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #Overwrite the validation of the form for creating a post:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#Class that permits the update of a post at the frontend of the site
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #Overwrite the validation of the form for creating a post:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

#Class that prevents another author from deleting a post that is not his
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #when a post is successfully deleted, redirect to home page
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


    
def aboutPage(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

