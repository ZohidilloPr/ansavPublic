from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    image = models.ImageField(default='user.png', upload_to='user_pic')

    def __str__(self):
        return f'{self.user} PROFILE'

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.width > 300 and img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)