from django.contrib import admin
from .models import Category
from .models import Updates,Booking
# Register your models here.
admin.site.register(Category)
admin.site.register(Updates)
admin.site.register(Booking)