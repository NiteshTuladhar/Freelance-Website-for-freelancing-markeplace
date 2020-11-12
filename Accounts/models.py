from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils import timezone
from datetime import datetime, date, timezone,timedelta
from .token import generatetoken



class AccountManager(BaseUserManager):
    def create_user(self, email, account_name,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        	account_name=account_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,account_name,password=None):
        user = self.create_user(
            email,
           
            password=password,
            account_name=account_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


    

class Account(AbstractBaseUser):
    email       = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    account_name        = models.CharField(max_length=100,unique=True)
    is_active           = models.BooleanField(default=True)
    is_admin            = models.BooleanField(default=False)
    send_first_email    = models.BooleanField(default=False)
    token               = models.CharField(blank=True,null=True, max_length=15)
    is_verified         = models.BooleanField(default=False)
    joined_on           = models.DateField(auto_now_add=True,null=True,blank=True)
    profile_create      = models.BooleanField(default=False)
    is_profile_set      = models.BooleanField(default=False)
    first_gig           = models.BooleanField(default=True)
    user_verified       = models.BooleanField(default=False)
    user_online         = models.BooleanField(default=False)
    last_logout         = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    is_available        = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'account_name' #This field must be used while doing login through authenticatie() function.
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.account_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



    def logout_last(self):
        diff = datetime.now(timezone.utc)-self.last_logout
        total_seconds = diff.total_seconds();
        if total_seconds<60:
            return  " a moment ago."
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


class Follow(models.Model):
    
    user            = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,blank=True)
    followed_to     = models.IntegerField()
    followed_by     = models.IntegerField()

    def save(self,*args,**kwargs):
        try:
            ft = Account.objects.get(id=self.followed_to)
            fb = Account.objects.get(id=self.followed_by)

            if self.followed_by == self.followed_to:
                return False
            else:
                super(Follow,self).save(*args,**kwargs)
                return True
        except:
            raise ValueError("No user found with this id")


    class Meta:
        unique_together = ('followed_to','followed_by')

    def __str__(self):
       return "followed_to "+ str(self.followed_to)+" | followed_by "+ str(self.followed_by)



def sendAccountCreationMail(sender, **kwargs):

    current_user        = kwargs['instance']

    if current_user.token is None:
        current_user.token = generatetoken()
        current_user.profile_create = True
        current_user.user_online = True
        current_user.save()


    current_user_mail   = current_user.email
    token               = current_user.token
    s                   = "Account Creation"



    context = {
        'id' : current_user.id,
        'name' : current_user.account_name,
        'subject' : s,
        'message' : "Your Account Has Been Created Successfully.",
        'token' : current_user.token
    }
    temp = get_template('welcomemail.html').render(context)
    email = EmailMessage(

        subject=s, 
        body=temp, 
        to= [current_user_mail]

        )

    email.content_subtype = 'html'

    

    try:
        if current_user.send_first_email==False:
            email.send()
            current_user.send_first_email=True
            current_user.save()
        else:
            pass  

    except:
        pass


post_save.connect(sendAccountCreationMail,sender=Account)




