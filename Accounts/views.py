from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def register(request):
	if request.method == 'POST':
		email = request.POST['email']
		account_name = request.POST['account_name']
		password = request.POST['password']
		if(len(password)>6):
			account = Account(email=email, account_name=account_name)
			account.set_password(password)
			try:
				account.save()
				messages.success(request,message="Your Account Has Been Created Successfully")
				return redirect('signin')
			except:
				messages.error(request,message="Sorry!!This Email Is Already In Use.")		
		else:
			messages.error(request,message="Password must be greater than 6 character long")
			return render(request,'register.html',{'email':email,'account_name':account_name})
			
	else:
		return render(request,'register.html')
		

	return render(request,'register.html')


def userlogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request,account_name=email,password=password)
		print(user)

		if user is not None:
			login(request, user)
			print('if')
			return redirect('homepage')
		else:
			print('else')
			messages.error(request,"Email or Password does not match")
			return redirect('signin')
	else:
		return render(request,'login.html')

	return render(request,'login.html')