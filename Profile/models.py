from django.db import models
from Accounts.models import Account
from django_countries.fields import CountryField
from languages.fields import LanguageField
from Accounts.models import Account
# Create your models here.
gender_list = [('Male','Male'), ('Female','Female'), ('Other','Other')]

class Language(models.Model):
	languages = models.CharField(default='Nepali', max_length=15, blank=True, null=True)

	def __str__(self):
		return self.languages

class MyProfile(models.Model):

    user = models.OneToOneField(Account,on_delete=models.CASCADE,default=1)
    full_name = models.CharField(max_length=10, null=True)
    country = CountryField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='user_img/',blank=True,null=True)
    gender = models.CharField(max_length=30,choices=gender_list)
    contact_no = models.CharField(max_length=15)
    skills = models.CharField(max_length=100,null=True,blank=True)
    languages = LanguageField(max_length=50,null=True,blank=True)
    google = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True,null=True)
    github = models.URLField(blank=True,null=True)





    def __str__(self):
        return self.full_name