from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Creation of post models
class Post(models.Model):
    #Title of the post
    title = models.CharField(max_length=100)
    #Content of the post:
    content = models.TextField()
    #Date of the creation of the post:
    date_posted = models.DateTimeField(default=timezone.now)
    #Author of the post:
    #If the author is delete then all of its posts are deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
