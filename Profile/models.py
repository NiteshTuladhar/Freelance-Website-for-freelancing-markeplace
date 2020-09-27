from django.db import models
from Accounts.models import Account

# Create your models here.
gender_list = [('Male','male'), ('Female','female'), ('Other','other')]

class Language(models.Model):
	languages = models.CharField(default='Nepali', max_length=15, blank=True, null=True)

	def __str__(self):
		return self.languages

class MyProfile(models.Model):
    username = models.CharField(max_length=10, null=True)
    full_name = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    profile_image = models.ImageField(upload_to='user_img/',blank=True,null=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=30,choices=gender_list)
    contact_no = models.CharField(max_length=15)
    member_since = models.DateField(auto_now=True)
    skills = models.CharField(max_length=100,null=True,blank=True)
    languages = models.ForeignKey(Language, on_delete=models.CASCADE)
    google = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True,null=True)
    github = models.URLField(blank=True,null=True)





    def __str__(self):
        return self.username