from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
'''welcome view to process landing page'''
def welcome(request):
    return render(request, 'index.html')
