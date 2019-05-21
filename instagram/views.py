from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, Profile
from .forms import NewPostForm, NewsProfileForm
from django.contrib.auth.decorators import login_required
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

'''function to enable user to post'''
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile=current_user
            post.save()
        return redirect('welcome')

    else:
        form = NewPostForm()
    return render(request, 'new_article.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
        return redirect('profile')
    else:
        form = NewsProfileForm()
    return render(request, 'new-profile.html', {"form":form})

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    return render(request, 'profile-page.html',{"profile":profile})
