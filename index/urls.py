from os import name
from re import template
# from re import template
from django.urls import path
from .views import home, reservation
from django.contrib.auth import views as auth_views

app_name = "index"

urlpatterns = [ 
    
    # path("", home, name = "index"),
    path("reservation/", reservation, name = "reserve"),
    # path("login/", auth_views.LoginView.as_view(template_name="index/login.html"), name= "login")
    # path("logout/", auth_views.LogoutView.as_view(template_name="index/logout.html"), name= "logout"),
    ] 

# Actual link

# http://127.0.0.1:8000/index/reservation/