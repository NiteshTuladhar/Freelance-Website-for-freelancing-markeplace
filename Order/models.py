from django.db import models
from Accounts.models import Account
from Gig.models import MyGig
from Profile.models import MyProfile

from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.template.loader import get_template
from autoslug import AutoSlugField
# Create your models here.

class MyOrder(models.Model):
	
    slug                = AutoSlugField(populate_from='gig',unique=True,null=True,blank=True) 
    gig                 = models.ForeignKey(MyGig,on_delete=models.SET_NULL, blank=True,null=True)
    customer            = models.ForeignKey(Account,on_delete=models.SET_NULL, blank=True,null=True)
    seller              = models.ForeignKey(Account,on_delete=models.SET_NULL, blank=True,null=True,related_name='seller')
    date_ordered        = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    transaction_id      = models.CharField(max_length=200,null=True)
    message             = models.CharField(max_length=2000,null=True)

    def __str__(self):
        return str(self.gig.title) + "  >>by  " + str(self.gig.user.account_name)+ "  >>ordered by  " +  str(self.customer)
       

    @property
    def get_total(self):
        total = self.gig.gig_price + 2
        return 



def sendOrderMail(sender, **kwargs):
    current_user        = kwargs['instance']
    current_user_mail   = current_user.customer.email

    

    s                   = "Thank You For The Purchase"
    context = {
        'id' : current_user.customer.id,
        'item' : current_user.gig.title,
        'name' : current_user.customer.account_name,
        'seller_name' : current_user.gig.user.account_name ,
        'date' : current_user.date_ordered,
        'price' : current_user.gig.price,
        'total_price' : current_user.gig.get_total,
        'time' : current_user.gig.time,
        'subject' : s,
        'message' : "Your recent Community Market purchase has been processed and your order has been placed.",
    }
    temp = get_template('buyersemail.html').render(context)
    email = EmailMessage(

        subject=s, 
        body=temp, 
        to= [current_user_mail]

        )

    email.content_subtype = 'html'

    email.send()
            

post_save.connect(sendOrderMail,sender=MyOrder)



def sendSellerMail(sender, **kwargs):
    current_user        = kwargs['instance']
    seller_user_mail    = current_user.gig.user.email

    s                   = "You have an order"
    context = {
        'id' : current_user.gig.user.id,
        'item' : current_user.gig.title,
        'buyer_name' : current_user.customer.account_name,
        'seller_name' : current_user.gig.user.account_name ,
        'date' : current_user.date_ordered,
        'price' : current_user.gig.price,
        'subject' : s,
        'message' : "A gig you listed in the Community Market has been ordered by",
    }
    temp = get_template('selleremail.html').render(context)
    email = EmailMessage(

        subject=s, 
        body=temp, 
        to= [seller_user_mail]

        )

    email.content_subtype = 'html'

    email.send()
            

post_save.connect(sendSellerMail,sender=MyOrder)