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
    image = models.ImageField(upload_to = 'articles/')
    image_name = models.CharField(max_length =50)
    image_caption = models.CharField(max_length =50)
    profile = models.ForeignKey(Profile)
    likes = models.CharField(max_length =50)
    comments = models.CharField(max_length =50)

    def __str__(self):
        return self.image_name

    '''return objects on database'''
    @classmethod
    def images_all(cls):
        posts = Image.objects.all()
        return posts

    '''save function'''
    def save_post(self):
        self.save()

    '''delete function'''
    def delete_post(self):
        self.delete()
