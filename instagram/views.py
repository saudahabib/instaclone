from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
# Create your views here.
'''welcome view to process landing page'''
def welcome(request):
    posts = Image.images_all()
    return render(request, 'index.html', {"posts":posts})
