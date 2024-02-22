from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

def index(request):
    if request.user.is_authenticated:
        # load all posts from all users. Sort by timestamp
        posts = Post.objects.all().order_by("-timestamp")
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
            post = Post(user=request.user, content=content)
            if request.POST["datetime"]:
                print("datetime found")
                datetime = request.POST["datetime"]
                post.published = datetime
                post.save()
            post.save()
        
        if "draft" in request.POST:
            print("draft clicked")
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
    pass
    # post = Post.objects.get(id=id)
    # if request.method == "POST":
    #     content = request.POST["content"]
    #     post.content = content
    #     post.save()
    #     return HttpResponseRedirect(reverse("index"))
    # else:
    #     return render(request, "social/edit_post.html", {
    #         "post" : post
    #     })
    
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse("index"))