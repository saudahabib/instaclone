from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImageTestClass(TestCase):
    '''Set up test object'''
    def setUp(self):
        self.image = Image(image ="" , image_name = "cute", image_caption="feelin cute" , likes = "3", comments = "wow, lookin fresh af")

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))


class ProfileTestClass(TestCase):
    '''Set up profile object'''
    def setUp(self):
        self.profile = Profile(profile_photo="", bio="random psycho")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
