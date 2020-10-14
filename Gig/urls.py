from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

path('mygig/',views.creategig,name='createusergig'),
path('edit-gig/<slug:slug>',views.editGig, name='editgig'),
path('<slug:slug>/delete',views.deleteGig,name='deletegig'),
path('<slug:slug>/',views.gigDetails,name='gigdetails'),
path('user-profile/<slug:slug>/',views.userDetails,name='userdetails'),
]

