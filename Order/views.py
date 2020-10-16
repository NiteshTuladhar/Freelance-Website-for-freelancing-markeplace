from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



def orderCheckout(request):

	return render(request,'order/order_checkout.html')