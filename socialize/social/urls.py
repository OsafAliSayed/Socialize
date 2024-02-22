from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    
    path("create_post", views.create_post, name="create_post"),
    path("drafts", views.drafts, name="drafts"),   
    
    path("edit_post/<int:id>", views.edit_post, name="edit_post"),
    path("delete_post/<int:id>", views.delete_post, name="delete_post"),
]