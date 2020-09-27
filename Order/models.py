from django.db import models
from Accounts.models import Account
from Gig.models import MyGig
from Profile.models import MyProfile

# Create your models here.

class MyOrder(models.Model):
	
	#customer = 
	username = models.ForeignKey(MyProfile, on_delete=models.CASCADE)
	date = models.DateField(auto_now=True)
	message = models.CharField(max_length=100)

	def __str__(self):
		return self.title