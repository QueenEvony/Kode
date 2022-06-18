
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  redirect
from .models import Reservation   
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == "POST":
        user_data=UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            messages.success(request, "Staff Added Successfully" )
            return redirect("index:index")
        else:
           messages.error(request, "Staff Declined" )
    context={
        "username":"admin",
        "gender":"female",
        "password":"admin1997",
        "email":"ex@gmail.com",
        "form": UserCreationForm()
        }
    return render(request, "index/index.html", context) 

def reservation(request):
     if request.method == "POST":
      Oname= request.POST.get("Oname")
      email=request.POST.get("email")
      amount=request.POST.get("amount")
      roomN=request.POST.get("roomN")
      Occupation=request.POST.get("Occupation")
      num_night=request.POST.get("num_night")
      ds= request.POST.get("ds")
      de=request.POST.get("de")
      reserve = Reservation(name=Oname,email=email,amount_paid=amount,roomNum=roomN,Occupation=Occupation,num_night=num_night,ds=ds,de=de)
      reserve.save()
      return redirect("index:index")
     return render(request, "index/entry.html")

 
# def login(request):
#     return render(request, "index/login.html") 
# Reservation.objects.all()
    # context = {
    #     "Reservation": Reservation
    #     # "Room_number": name,
    #     # "amount paid" :,
    #     # "name":,
    #     # "email":
    #     # "Occupation":
    #     # "Num_nights":
    #     # "Start date":
    #     #  "End Date" :
    # }