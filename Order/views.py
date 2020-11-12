from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Gig.models import MyGig,Review
from Order.models import MyOrder
from Accounts.models import Account
import datetime

def orderCheckout(request,slug):
	
	gig = MyGig.objects.get(slug=slug)
	review = Review.objects.filter(gigs=gig, reply=None).order_by('-comment_time')
	id  = gig.user_id

	

	context = {

		'gig' : gig,
		'id' : id,
		'review' : review,
	}

	return render(request,'order/order_checkout.html',context)


def orderCheckoutMessage(request,slug):

	gig = MyGig.objects.get(slug=slug)
	review = Review.objects.filter(gigs=gig, reply=None).order_by('-comment_time')

	id  = gig.user_id


	context = {

		'gig' : gig,
		'id' : id,
		'review' : review,
		
	}

	return render(request,'order/order_message.html',context)


def orderCheckoutComplete(request,slug):

	gig = MyGig.objects.get(slug=slug)
	id  = gig.user_id
	seller = Account.objects.get(id=id)
	message = request.POST.get('message')
	print(message)
	print('+++++++++++++++++++++++')

	order_id = datetime.datetime.now().timestamp()

	order = MyOrder.objects.create(customer=request.user,gig=gig,message=message,seller=seller)
	order.transaction_id = order_id
	order.save()

	myorder = MyOrder.objects.get(slug=slug)
	context = {

		'gig' : gig,
		'id' : id,
		'myorder' : myorder,
		
	}

	return render(request,'order/order_complete.html',context)






	