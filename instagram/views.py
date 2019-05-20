from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
# Create your views here.
'''welcome view to process landing page'''
def welcome(request):
    posts = Image.images_all()
    return render(request, 'index.html', {"posts":posts})

def search_results(request):
    if 'image_name' in request.GET and request.GET["image_name"]:
        search_term = request.GET.get("image_name")
        searched_posts = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-posts/search.html', {"message":message,"posts": searched_posts})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html',{"message":message})
