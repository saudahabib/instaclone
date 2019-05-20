from .models import Image

class NewPostForm(form.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'comments', 'profile']
        
