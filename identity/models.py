from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import UserManager

# Create your models here.

#Meta class to store timezone info
class Timezone(models.Model):
    created_at = models.DateTimeField(default=timezone.now,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    

    class Meta:
        abstract = True

# User model Class for creating a user ans
class User(AbstractBaseUser,PermissionsMixin,Timezone):

    user_type = [
    ('Student','Student'),
    ('Admin','Admin'),
    ]

    first_name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    email = models.EmailField(null=False,unique=True)
    user_profile = models.CharField(max_length=255,choices=user_type,default=user_type[0][0],null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email