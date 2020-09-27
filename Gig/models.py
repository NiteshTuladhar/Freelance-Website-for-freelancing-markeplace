from django.db import models
from Accounts.models import Account
from Profile.models import MyProfile

# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.c_name

class SubCategory(models.Model):
    s_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sub_category/')
    c_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name

class MyGig(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	search_tag = models.CharField(max_length=15)
	price= models.FloatField()
	time = models.TimeField(auto_now=True)
	contact_no = models.ForeignKey(MyProfile, on_delete=models.CASCADE)
	s_name = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.title