from django.shortcuts import render,redirect




def login_homepage(request):

	if request.user.is_authenticated:
		return render(request,'userhome.html')
		print(user.is_authenticated)
	else:
		return render(request,'index.html')