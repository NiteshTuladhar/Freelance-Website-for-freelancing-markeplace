from django.db import models
from Accounts.models import Account
from Profile.models import MyProfile
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils.timezone import now
from datetime import datetime, date, timezone
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
    description     = models.CharField(max_length=1000)
    gig_image       = models.ImageField(upload_to='gig_profile_img',blank=True,null=True)
    c_name          = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    created_on      = models.DateTimeField(auto_now=True,blank=True,null=True)
    search_tag      = models.CharField(max_length=15)
    price           = models.FloatField()
    time            = models.IntegerField(null=True,blank=True)
    s_name          = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)
    liked           = models.ManyToManyField(Account,default=None,related_name='post_like',blank=True)
    favourite       = models.ManyToManyField(Account,related_name='favourites',blank=True)
    
    def __str__(self):
        return self.title

    def gig_duration(self):
        diff = datetime.now(timezone.utc)-self.created_on
        total_seconds = diff.total_seconds();
        if total_seconds<60:
            return str(int(total_seconds)) + " seconds ago."
        elif total_seconds<=3600:
            minute = total_seconds/60
            return str(int(minute))+ " minutes ago."
        elif total_seconds<86400:
            hrs = (total_seconds/60)/60
            return str(int(hrs))+ " hrs ago."
        elif total_seconds<2592000:
            days = ((total_seconds/60)/60)/24
            return str(int(days))+ " days ago."
        elif total_seconds<31104000:
            months = (((total_seconds/60)/60)/24)/30
            return str(int(months))+ " months ago."
        else :
            year = ((((total_seconds/60)/60)/24)/30)/12
            return str(int(year))+ " year ago."

        return diff.total_seconds()

    @property
    def num_likes(self):
        return self.likes.all().count()


LIKE_CHOICES = {
    ('Like','Like'),
    ('Unlike','Unlike'),
} 


class Likes(models.Model):
    user            = models.ForeignKey(Account,on_delete=models.CASCADE)
    gigs            = models.ForeignKey(MyGig,on_delete=models.CASCADE,null=True,blank=True)
    value           = models.CharField(choices=LIKE_CHOICES, default='Like',max_length=10)

    def __str__(self):
        return str(self.gigs)
 

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


class Saves(models.Model):
    user            = models.ForeignKey(Account,on_delete=models.CASCADE)
    gigs            = models.ForeignKey(MyGig,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.gigs)