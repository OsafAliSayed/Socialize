from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
# Table that holds user data
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}, {self.username}, {self.email}"
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    published = models.DateTimeField(default=datetime.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id}, {self.user}, {self.content}, {self.timestamp}, {self.is_draft}"