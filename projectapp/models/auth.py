from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager,PermissionsMixin

class CustomUserManager(UserManager):
    def create_user(self,email,password=None,is_staff=False,is_superuser=False,**extra_fields):
        user=self.model(email=email,password=password,
                        is_staff=is_staff,is_superuser=is_superuser,
                        **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email , password, **extra_fields):
        return self.create_user( email, password,is_staff=True,is_superuser=True, perm=True,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    
    perm = models.BooleanField(default=False,blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    
    
    USERNAME_FIELD = "email"



class OTP(models.Model):
    key = models.CharField(max_length=1024)
    email = models.CharField(max_length=512)
    is_expire = models.BooleanField(default=False)
    tries = models.SmallIntegerField(default=0)
    step = models.CharField(max_length=26)
    by = models.IntegerField(choices=[
        (1,"By register"),
        (2,"By login")
    ])    
    created = models.DateTimeField(auto_now=False,auto_now_add=True,editable=False)
    created = models.DateTimeField(auto_now=True,auto_now_add=False,editable=False)

    def save(self,*args, **kwargs):
        if self.tries >= 3:
            self.is_expire = True
        return super(OTP,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.email
    