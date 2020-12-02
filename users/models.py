from django.db import models
from django.contrib.auth.models import User


#One to One relationship between a profile and a user:
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #We can add any attributes of the profile we want (adress number, email, ...)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #Returns a more human readable object of the profile:
    def __str__(self):
        return f'{self.user.username} Profile'
