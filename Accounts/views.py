from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Account, Follow
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .token import generatetoken
from django.utils.safestring import mark_safe
from Profile.models import MyProfile
from Gig.models import MyGig, Category, SubCategory
from datetime import datetime, date, timezone
from Order.models import MyOrder

import requests 

# Create your views here.
#User Registration.
def register(request):
	if request.method == 'POST':
		email = request.POST['email']
		account_name = request.POST['account_name']
		password = request.POST['password']

		##Captcha verification##

		##pip install requests
		##add import requests at top
		
		captcha_token = request.POST.get("g-recaptcha-response")
		cap_url = "https://www.google.com/recaptcha/api/siteverify"
		cap_secret = "6LfqcesZAAAAALg54FPrgbPXRysOtSZWqunp2bT_"
		cap_data = {"secret":cap_secret,"response":captcha_token}
		cap_server_response = requests.post(url=cap_url,data=cap_data)
		print("--------------------------------")
		print(cap_server_response.text)
		print("--------------------------------")

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

def verifyaccount(request,id,token,backend='django.contrib.auth.backends.ModelBackend'):

	a = Account.objects.get(id=id)

	if a.is_verified == False:

		if a.token == token:
			a.is_verified = True
			a.save()
			login(request, a, backend='django.contrib.auth.backends.ModelBackend')
			if a.profile_create is True:
					profile = MyProfile(user=request.user)
					a.profile_create = True
					profile.save()
					a.save()
			messages.success(request,mark_safe("Your account is activated. Hey!! It's a great time to <a href="" >create your profile.</a>"))#mark_safe is used to allow link in a messages

		else:
			messages.error( request,message="Error occured ")

		return redirect('userhome')

	else:
		messages.success(request,mark_safe("Your account is already activated. Hey!! It's a great time to <a href="">create your profile.</a>"))
		return render(request,'userhome.html')

	return redirect('userhome')




#User Lgoin
def userlogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request,account_name=email,password=password)#Here acccount_name chai hamro REQUIRED_FIELD bata ayo ani email chai hamro form ko data
		

		if user is not None:


			login(request, user)

			acc = Account.objects.get(id=request.user.id)
			acc.user_online = True
			acc.save()
			
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
	account = Account.objects.get(id=request.user.id)
	account.user_online = False
	account.last_logout = datetime.now(timezone.utc)
	account.save()
	
	logout(request)
	return redirect('homepage')



@login_required
def userHome(request):
	gigs = MyGig.objects.exclude(id=request.user.id)[:4]
	nextgigs = MyGig.objects.exclude(id=request.user.id)[4:8]
	account = Account.objects.all()
	profile = MyProfile.objects.all()
	catergories = Category.objects.all()


	x= Follow.objects.filter(followed_by=request.user.id).values('followed_to')
	followers_list = []
	for y in x:
		followers_list.append(y['followed_to'])

	non_followers = MyGig.objects.exclude(user_id__in=followers_list)
	followers = MyGig.objects.filter(user_id__in=followers_list)
	print(non_followers)
	print(followers)

	completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')

	available_for_withdrawal = 0;

	for order in completed_orders:

		available_for_withdrawal += order.gig.price

	context = {

		'gigs' : gigs,
		'nextgigs' : nextgigs,
		'account'  : account,
		'profile' : profile,
		'catergories' : catergories,
		'non_followers' : non_followers,
		'followers' : followers,
		'available_for_withdrawal' : available_for_withdrawal
	}

	return render(request,'userhome.html',context)


"""
def homepage(request):
	 
	if user.is_authenticated:
		return redirect('dashboard')
	else:
		return render(request,'index.html')

	return render(request,'index.html')
"""


