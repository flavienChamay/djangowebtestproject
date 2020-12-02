from django.contrib import admin
from .models import Profile

#We add the Profile class within our admin page (it will make our picture incorporate in the registration form)
admin.site.register(Profile)
