from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

path('mygig/',views.creategig,name='createusergig'),
path('edit-gig/<slug:slug>',views.editGig, name='editgig'),
path('<slug:slug>/delete',views.deleteGig,name='deletegig'),
path('<slug:slug>/',views.gigDetails,name='gigdetails'),
path('<slug:slug>/',views.othersgigDetails,name='othersgigdetails'),

path('like',views.like_gig, name='like-gig'),
path('favourite',views.save_gig,name='save-gig'),


]

