from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImageTestClass(TestCase):
    '''Set up test object'''
    def setUp(self):

        '''creating a new profile and saving it'''
        self.profile = Profile(profile_photo="", bio="queen ui")
        self.profile.save_profile()

        '''creating a new post and saving it'''
        self.image = Image(image ="" , image_name = "cute", image_caption="feelin cute" ,profile=self.profile,likes = "3", comments = "wow, lookin fresh af")
        self.image.save()

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()

    '''Test to check instance created'''
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    '''Test to check if save function works'''
    def test_save_post(self):
        self.image.save_post()
        posts = Image.objects.all()
        self.assertTrue(len(posts)>0)

    '''test to check if delete function works'''
    def test_delete_post(self):
        self.image.delete_post()
        posts = Image.objects.all()
        self.assertTrue(len(posts)==0)

    
class ProfileTestClass(TestCase):
    '''Set up profile object'''
    def setUp(self):
        self.profile = Profile(profile_photo="", bio="random psycho")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
