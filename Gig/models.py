from django.db import models
from Accounts.models import Account
from Profile.models import MyProfile
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils.timezone import now
from datetime import datetime
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    c_name          = models.CharField(max_length=100)
    description     = models.CharField(max_length=100)

    def __str__(self):
        return self.c_name

class SubCategory(models.Model):
    s_name              = models.CharField(max_length=100)
    description         = models.CharField(max_length=100)
    image               = models.ImageField(upload_to='sub_category/')
    c_name              = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name

class MyGig(models.Model):

    user            = models.ForeignKey(Account,on_delete=models.CASCADE,default=1)
    profile         = models.ForeignKey(MyProfile,on_delete=models.CASCADE,null=True,blank=True)
    title           = models.CharField(max_length=100)
    slug            = AutoSlugField(populate_from='title',unique=True,null=True,blank=True)
    description     = models.CharField(max_length=100)
    gig_image       = models.ImageField(upload_to='gig_profile_img',blank=True,null=True)
    c_name          = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    created_on      = models.DateField(default=datetime.now,null=True,blank=True)
    search_tag      = models.CharField(max_length=15)
    price           = models.FloatField()
    time            = models.IntegerField(null=True,blank=True)
    s_name          = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)
    likes           = models.ManyToManyField(Account, related_name='post_likes', blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gigdetails", kwargs={"slug": self.slug})


class Review(models.Model):

    user                = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    profile             = models.ForeignKey(MyProfile,on_delete=models.CASCADE,null=True,blank=True)
    gigs                = models.ForeignKey(MyGig,on_delete=models.CASCADE,null=True,blank=True)
    message             = models.TextField()
    reply               = models.ForeignKey('Review', null=True, related_name='replies',on_delete=models.CASCADE,blank=True)# Here Instead of 'Review' you can also do 'self'. and related_name='replies' will help- to query the replies of the related comments.
    is_approved         = models.BooleanField(default=False)
    comment_time        = models.DateTimeField(auto_now_add=True)


    def __srt__(self):
        return format(self.gigs.title)