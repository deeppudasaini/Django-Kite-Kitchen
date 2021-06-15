from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def userPage(request):
  
    return render(request,"index.html")
def aboutUs(request):
    return render(request,"about.html")

def categories(request):
    return render(request,"category.html")