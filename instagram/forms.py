from .models import Image
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'comments', 'profile']

class NewProfileForm(form.ModelForm):
    class Meta:
        model = Profile