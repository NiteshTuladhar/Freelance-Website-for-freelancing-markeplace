from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

path('<slug:slug>/ordercheckout/',views.orderCheckout,name='order'),
path('<slug:slug>/ordermessage/',views.orderCheckoutMessage,name='ordercheckoutmessage'),
path('<slug:slug>/ordercomplete/',views.orderCheckoutComplete,name='ordercheckoutcomplete'),

]

