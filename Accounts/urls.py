"""Freelance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #view as auth_view is done as we have another imported view above so in order to above conflict.
from django.conf.urls import url, include

urlpatterns = [
    #path('',views.homepage,name='homepage'),
	path('register/', views.register, name='register'),
    path('account-verify/<int:id>/<str:token>/',views.verifyaccount,name='verify_token'),
	path('login/', views.userlogin, name='signin'),
	path('logout/',views.userlogout, name='logout'),
	path('home/',views.userHome, name='userhome'),
    path('reset-password/',auth_views.PasswordResetView.as_view(
        template_name='account/password_reset_form.html',
        #email_template_name='account/email_template.html'
        ),name='reset_password'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html'
        ),name='password_reset_confirm'),
    path('reset-sent/',auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_email_sent.html'
        ),name='password_reset_done'),
    path('reset-complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'
        ),name='password_reset_complete'),

    url(r'^oauth/', include('social_django.urls', namespace='social')),
 ]
    
