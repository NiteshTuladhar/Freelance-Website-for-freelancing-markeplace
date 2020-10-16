from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

path('ordercheckout/',views.orderCheckout,name='order'),
]

