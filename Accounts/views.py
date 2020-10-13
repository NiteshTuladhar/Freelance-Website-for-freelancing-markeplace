from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .token import generatetoken
from django.utils.safestring import mark_safe
from Profile.models import MyProfile


# Create your views here.
#User Registration.
def register(request):
	if request.method == 'POST':
		email = request.POST['email']
		account_name = request.POST['account_name']
		password = request.POST['password']
		if(len(password)>6):
			account = Account(email=email, account_name=account_name)
			account.set_password(password)
			try:
				account.token = generatetoken()
				account.save()
				messages.success(request,message="Your Account Has Been Created Successfully. Please Check Your Mail To Verify Your Account.")
				return redirect('signin')
			except:
				messages.error(request,message="Sorry!!This Email Is Already In Use.")		
		else:
			messages.error(request,message="Password must be greater than 6 character long")
			return render(request,'register.html',{'email':email,'account_name':account_name})
			
	else:
		return render(request,'register.html')
		

	return render(request,'register.html')



#Sends Email with token to verify account.

def verifyaccount(request,id,token):

	a = Account.objects.get(id=id)

	if a.is_verified == False:

		if a.token == token:
			a.is_verified = True
			a.save()
			login(request, a)
			if a.profile_create is False:
					profile = MyProfile(user=request.user)
					a.profile_create = True
					profile.save()
					a.save()
			messages.success(request,mark_safe("Your account is activated. Hey!! It's a great time to <a href="" >create your profile.</a>"))#mark_safe is used to allow link in a messages

		else:
			messages.error( request,message="Error occured ")

		return render(request,'userhome.html')

	else:
		messages.success(request,mark_safe("Your account is already activated. Hey!! It's a great time to <a href="">create your profile.</a>"))
		return render(request,'userhome.html')

	return render(request,'userhome.html')




#User Lgoin
def userlogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request,account_name=email,password=password)#Here acccount_name chai hamro REQUIRED_FIELD bata ayo ani email chai hamro form ko data
		

		if user is not None:
			login(request, user)
			acc = Account.objects.get(id=request.user.id)

			
			if acc.profile_create is False:
				profile = MyProfile(user=request.user)
				acc.profile_create = True
				profile.save()
				acc.save()
				if acc.is_verified:
					return redirect('userhome')
			else:
				return redirect('userhome')
			
		else:
			messages.info(request,"Email or Password does not match")
			return redirect('signin')
	else:
		return render(request,'login.html')

	return render(request,'login.html')

def userlogout(request):
	logout(request)
	return redirect('homepage')

@login_required
def userHome(request):

	return render(request,'userhome.html')



"""
def homepage(request):
	 
	if user.is_authenticated:
		return redirect('dashboard')
	else:
		return render(request,'index.html')

	return render(request,'index.html')
"""


