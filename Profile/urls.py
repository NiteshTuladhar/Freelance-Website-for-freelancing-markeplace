from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

path('profile/',views.userprofile,name='userprofile'),
path('userprofile/<int:id>',views.completeuserprofile,name='compuserprofile'),
path('changeprofilepic/',views.changeprofilepic,name='changeprofilepic'),
path('edit-profile/',views.editProfile,name='editprofile'),
path('myprofile/<int:id>',views.myProfile,name='mygig'),
path('visitprofile/<int:id>',views.userProfile,name='visitprofile'),
path('follow/<int:id>/',views.followUser,name='followuser'),
path('unfollow/<int:id>/',views.unfollowUser,name='unfollowuser'),

path('liked_gigs/',views.liked_gigs,name='liked_gigs'),
path('saved/',views.saved_gigs,name='saved_gigs'),
path('',views.availability,name='availability'),
path('myorders/',views.myOrders,name='myorders'),
path('myordersdetails/<slug:slug>',views.myOrdersDetails,name='myordersdetails'),
#path('follow/',views.myFollowFollowing,name='followfollowing'),
path('buyer_orders/',views.buyerOrders,name='buyerorder'),
path('buyers_orders_details/<slug:slug>',views.buyersOrdersDetails,name='buyers_orders_details'),

path('buyers_orders_details/<slug:slug>/complete',views.complete_order,name='complete_order'),
path('buyers_orders_details/<slug:slug>/cancelled',views.cancel_order,name='cancel_order'),

path('earnings/',views.userEarnings,name='userearnings'),
path('analytics/',views.userAnalytics,name='useranalytics'),
]

