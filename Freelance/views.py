from django.shortcuts import render,redirect
from Gig.models import MyGig



def login_homepage(request):
	gigs = MyGig.objects.all()
	context = {
		'gigs' : gigs

	}
	if request.user.is_authenticated:
		return render(request,'userhome.html',context)
		print(user.is_authenticated)
	else:
		return render(request,'index.html',context)