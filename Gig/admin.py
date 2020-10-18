from django.contrib import admin
from .models import Category, SubCategory,MyGig,Review
# Register your models here.
admin.site.register([Category, SubCategory,MyGig,Review])