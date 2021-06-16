from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Updates(models.Model):
    updateTitle=models.CharField(max_length=50)
    updateDescription=models.CharField( max_length=150)
    updateDates=models.DateField()
    def __str__(self):
        return self.updateTitle

class Booking(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField( max_length=150)
    phone=models.CharField(max_length=30)
    numberOfGuest=models.IntegerField()
    bookDate=models.DateField()
    def __str__(self):
        return self.name
class Menu(models.Model):
    name=models.CharField(max_length=50)
    desciption=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
