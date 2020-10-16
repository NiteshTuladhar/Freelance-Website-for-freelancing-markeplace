from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

path('profile/',views.userprofile,name='userprofile'),
path('userprofile/<int:id>',views.completeuserprofile,name='compuserprofile'),
path('changeprofilepic/',views.changeprofilepic,name='changeprofilepic'),
path('edit-profile/',views.editProfile,name='editprofile'),
path('myprofile/<int:id>',views.myProfile,name='mygig'),
path('visitprofile/<int:id>',views.userProfile,name='visitprofile')
]

