from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'articles/', blank = True)
    bio=models.CharField(max_length =50)

    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/', blank = True)
    image_name = models.CharField(max_length =50)
    image_caption = models.CharField(max_length =50)
    profile = models.ForeignKey(Profile)
    likes = models.CharField(max_length =50)
    comments = models.CharField(max_length =50)

    def __str__(self):
        return self.image_name

    '''save function'''
    def save_post(self):
        self.save()
