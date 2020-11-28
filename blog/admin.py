#This is where we register our models so that we can see them in our admin page

from django.contrib import admin
from .models import Post

#Register the models
admin.site.register(Post)
