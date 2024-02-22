from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

from django.utils import timezone
from bs4 import BeautifulSoup
def index(request):
    
    if request.user.is_authenticated:
        # load all posts from all users. Sort by timestamp
        # check if published date is passed
        posts = Post.objects.all()
        posts = posts.filter(published__lte=timezone.now())
        return render(request, "social/index.html", {
            "posts" : posts,
            "user" : request.user
        })
    return render(request, "social/index.html", {
        "user" : request.user
    })
    
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "social/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "social/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "social/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "social/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "social/register.html")

def create_post(request):
    if request.method == "POST":
        # if user clicked submit button
        if "submit" in request.POST:
            content = request.POST["content"]
            # check if post is from draft 
            
            if "id" in request.POST:
                post = Post.objects.get(id=request.POST["id"])
                post.content = content
                post.is_draft = False
                if request.POST["datetime"]:
                    post.published = request.POST["datetime"]
                else:
                    post.published = timezone.now()

                post.save()
            else:
                post = Post(user=request.user, content=content)
                if request.POST["datetime"]:
                    datetime = request.POST["datetime"]
                    post.published = datetime
                    post.save()
                post.save()
        
        if "draft" in request.POST:

            content = request.POST["content"]
            post = Post(user=request.user, content=content, is_draft=True)
            post.save() 
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "social/create_post.html")
    
def drafts(request):
    drafts = Post.objects.filter(user=request.user, is_draft=True)
    print(drafts)
    return render(request, "social/drafts.html", {
        "drafts" : drafts
    })
    
def edit_post(request, id):
    return render(request, "social/create_post.html", {
        "post" : Post.objects.get(id=id)
    })
    
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse("index"))

def scheduled_post(request):
    posts = Post.objects.filter(user=request.user)
    posts = posts.filter(published__gt=timezone.now())
    return render(request, "social/scheduled_post.html", {
        "drafts" : posts
    })