from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Gig.models import MyGig,Review
from Order.models import MyOrder


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
	message = request.POST.get('message')
	print(message)
	print('+++++++++++++++++++++++')
	
	id  = gig.user_id

	order = MyOrder.objects.create(customer=request.user,gig=gig,message=message)
	order.save()


	context = {

		'gig' : gig,
		'id' : id,
		
	}

	return render(request,'order/order_complete.html',context)






	