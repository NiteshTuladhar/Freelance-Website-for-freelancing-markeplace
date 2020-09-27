from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

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
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    account_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
   


    objects = AccountManager()

    USERNAME_FIELD = 'account_name'
    REQUIRED_FIELDS = ['email','account_name']

    def __str__(self):
        return self.account_name

   