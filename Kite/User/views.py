from django.shortcuts import render,redirect,HttpResponse
from .models import Category,Updates,Booking
# Create your views here.
def userPage(request):
    variables=    {
        'categories':Category.objects.all(),
        'updates':Updates.objects.all()
    };
    return render(request,"index.html",variables)
def aboutUs(request):
    return render(request,"about.html")

def categories(request):
    variables=    {
        'categories':Category.objects.all()
    };
    return render(request,"category.html",variables)

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

    