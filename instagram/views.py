from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from .forms import NewPostForm, NewProfileForm
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
    posts = Image.objects.filter(profile=current_user)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.profile=current_user
            profile.save()
        return redirect('profile-page')

    else:
        form = NewProfileForm()
    return render(request, 'profile-page.html', {"posts":posts})
