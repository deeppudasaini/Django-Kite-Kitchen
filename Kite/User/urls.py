"""Kite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from User import views
urlpatterns = [
path("",views.userPage,name="User Page"),
path("about",views.aboutUs,name="About Us"),
path("category/<int:idOfMenu>/",views.categories,name="categories"),
path("booking",views.book,name="booking"),
path("dish/<int:idOfDish>",views.dishPage,name="Dish"),
path("login",views.Login,name="Login"),
path("logout",views.Logout,name="Login"),
]
