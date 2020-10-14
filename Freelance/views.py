from django.shortcuts import render,redirect
from Gig.models import MyGig
from Accounts.models import Account
from Profile.models import MyProfile


def login_homepage(request):
	gigs = MyGig.objects.all()
	account = Account.objects.all()
	profile = MyProfile.objects.all()
	context = {
		'gigs' : gigs,
		'account' : account,
		'profile' : profile,

	}
	if request.user.is_authenticated:
		return render(request,'userhome.html',context)
		print(user.is_authenticated)
	else:
		return render(request,'index.html',context)


def search(request):
	query_text = request.GET.get('q')
	result = MyGig.objects.filter(title__icontains=query_text)

	context = {
		'query_text' : query_text
	}
	if(len(result)) == 0:
		context.update({'noresult' : 'No services were found'})

	else:
		context.update({'result' : result})
	return render(request,'searchresult.html',context)