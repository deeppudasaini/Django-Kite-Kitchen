from django.shortcuts import render,redirect,HttpResponse
from .models import Category,Updates,Booking,Menu,Staff
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
# Create your views here.
def userPage(request):
    
    variables=    {
        'categories':Category.objects.all(),
        'updates':Updates.objects.all()
    };
    return render(request,"index.html",variables)
def aboutUs(request):
    return render(request,"about.html")

def categories(request,idOfMenu):
        menus=Menu.objects.filter(category=idOfMenu)
        variables=    {
            'categories':Category.objects.all(),
            'menus':menus
        };
        return render(request,"category.html",variables)

def dishPage(request,idOfDish):
    variables={
        'menuInfo':Menu.objects.filter(id=idOfDish),
        'categories':Category.objects.all(),
    }
    return render(request,"dish.html",variables)

def book(request):
    if request.method=="POST":
        bookerName=request.POST['name']
        bookerAddress=request.POST['address']
        bookerPhone=request.POST['number']
        bookerNumber=request.POST['guest']
        bookerDate=request.POST['datetime']
        singleRow=Booking(name=bookerName,address=bookerAddress,phone=bookerPhone,numberOfGuest=bookerNumber,bookDate=bookerDate)
        singleRow.save()
        return redirect("/")
    else:
        return render(request,"booking.html")

    
def Login(request):
    if request.method=='POST':  
        user=request.POST['username']
        passwor=request.POST['password']
        auth=authenticate(username=user,password=passwor)
        if auth is not None:   
            login(request,auth)
            return redirect("/")
    else:
        return render(request,"login.html")
def Logout(request):
    logout(request)
    return redirect("/")