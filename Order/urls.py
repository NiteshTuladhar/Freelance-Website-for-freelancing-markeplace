from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import View




urlpatterns = [

path('<slug:slug>/ordercheckout/',views.orderCheckout,name='order'),
path('<slug:slug>/ordermessage/',views.orderCheckoutMessage,name='ordercheckoutmessage'),
path('<slug:slug>/payment_method/',views.paymentProcess,name='paymentprocess'),
path('<slug:slug>/ordercomplete/',views.orderCheckoutComplete,name='ordercheckoutcomplete'),

path('khalti-verify/', views.khaltiVerify, name='khalti-verify'),


]


