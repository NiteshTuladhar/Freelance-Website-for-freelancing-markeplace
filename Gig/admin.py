from django.contrib import admin
from .models import Category, SubCategory,MyGig
# Register your models here.
admin.site.register([Category, SubCategory,MyGig])