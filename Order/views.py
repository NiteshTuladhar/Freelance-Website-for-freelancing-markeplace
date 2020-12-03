from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Gig.models import MyGig,Review
from Order.models import MyOrder
from Accounts.models import Account
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests

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



def paymentProcess(request, slug):

	gig = MyGig.objects.get(slug=slug)
	id  = gig.user_id
	seller = Account.objects.get(id=id)
	message = request.POST.get('message')
	
	print('---------message---------------')
	print(message)
	print('-------------------------------')

	order_id = datetime.datetime.now().timestamp()

	order , created = MyOrder.objects.get_or_create(customer=request.user,gig=gig,message=message,seller=seller)
	order.transaction_id = order_id
	order.save()

	myorder = MyOrder.objects.get(slug=slug)
	context = {

		'gig' : gig,
		'id' : id,
		'myorder' : myorder,
		
	}
	return render(request,'payment_methods.html',context)


@csrf_exempt
def khaltiVerify(request):

	data = request.POST

	token = data["token"]
	amount =data["amount"]
	o_id = data["product_identity"]

	print('---------payload data---------------')
	print(token, amount, o_id)
	print('---------------------------------------')

	url = "https://khalti.com/api/v2/payment/verify/"
	payload = {
	  "token": token,
	  "amount": amount
	}
	headers = {
	  "Authorization": "Key test_secret_key_6ff60dcc167d4842bf4a84cca67480a9"
	}

	myorder = MyOrder.objects.get(id=o_id)

	print('---------my order---------------')
	print(myorder)
	print('---------------------------------------')


	response = requests.post(url, payload, headers = headers)

	print('---------response status---------------')
	print(response)
	print('---------------------------------------')


	resp_dict = response.json()

	print('---------response data---------------')
	print(resp_dict)
	print('-------------------------------------')
		
	if resp_dict.get("idx"):
		success = True
		print('0000000000000')
		print(myorder.payment_complete)
		myorder.payment_complete = 'Transaction Completed'
		myorder.payment_method = "Khalti"
		myorder.save()
	else:
		success = False
	data = {
		"Success" : success
	}
	return JsonResponse(data)



def orderCheckoutComplete(request,slug):

	gig = MyGig.objects.get(slug=slug)
	id  = gig.user_id
	seller = Account.objects.get(id=id)

	myorder = MyOrder.objects.get(slug=slug)
	context = {

		'gig' : gig,
		'id' : id,
		'myorder' : myorder,
		
	}

	return render(request,'order/order_complete.html',context)


