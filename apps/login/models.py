from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def reg_validate(self,data):
        errors=[]
        if len(data['f_name'])<1:
            errors.append('First name too short. Enter a valid name.')
        if len(data['l_name'])<1:
            errors.append('Last name too short. Enter a valid name.')
        if data['password']!=data['repass']:
            errors.append('Passwords do not match. Passwords need to match.')
        pass

class User(models.Model):
    f_name=models.CharField(max_length=40)
    l_name=models.CharField(max_length=40)
    u_name=models.CharField(max_length=30)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
objects=UserManager()

# Create your models here.
