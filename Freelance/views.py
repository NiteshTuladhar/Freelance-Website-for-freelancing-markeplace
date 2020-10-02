from django.shortcuts import render,redirect



def nonlogin_homepage(request):

	return render(request,'index.html')

def login_homepage(request):
	return render(request,'dashboard.html')