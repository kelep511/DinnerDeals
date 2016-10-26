from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from django.core.exceptions import ObjectDoesNotExist
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def user_validate(self,data):
        errors=[]
        self.user_check(data['u_name'],errors)
        self.pass_val(data['password'],errors)
        if errors:
            return errors
        try:
            user= self.get(u_name=data['u_name'].title())
            print user.u_name
            if bcrypt.hashpw(data['password'].encode(),user.password.encode())==user.password.encode():
                return (False,user)
            else:
                errors.append('User name and/or password is incorrect')
                return errors
        except ObjectDoesNotExist:
            errors.append('User name and/or password is incorrect')
            return errors

    def reg_validate(self,data):
        errors=[]
        users=self.all()
        for user in users:
            if data['email'].title()==user.email:
                errors.append('Email address taken')
                break
        for user in users:
            if data['u_name'].title()==user.u_name:
                errors.append('Username already taken')
                break

        self.f_name_check(data['f_name'],errors)
        self.l_name_check(data['l_name'],errors)
        self.email_check(data['email'],errors)
        self.user_check(data['u_name'],errors)
        self.zip_check(data['zip'],errors)
        self.pass_check(data['password'], data['repass'],errors)
        self.pass_val(data['password'],errors)
        return errors
    def edit_user(self,data):
        errors=[]
        changes={

        }

        if data['f_name']:
            self.f_name_check(data['f_name'],errors)
            changes['f_name']=data['f_name'].title()
        if data['l_name']:
            self.l_name_check(data['l_name'],errors)
            changes['l_name']=data['l_name'].title()
        if data['email']:
            self.email_check(data['email'],errors)
            users=self.all()
            for user in users:
                if data['email'].title()==user.email:
                    errors.append('Email address taken')
                    break
            changes['email']=data['email'].title()
        if data['zip']:
            self.zip_check(data['zip'],errors)
            zip_code=data['zip'].zfill(5)
            changes['z_code']=data['zip']

        if data['password']:
            self.pass_val(data['password'],errors)
            self.pass_check(data['password'], data['repass'],errors)
            hashed_pw=bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            changes['password']=hashed_pw
        return errors, changes



    def f_name_check(self,f_name, errors):
            if len(f_name)<2:
                errors.append('First name too short. Enter a valid name.')
            return self
    def l_name_check(self,l_name, errors):
            if len(l_name)<1:
                errors.append('Last name too short. Enter a valid name.')
            return self
    def email_check(self,email, errors):
            if not re.match(EMAIL_REGEX, email):
                errors.append("Email is not a valid address. Please try again")
            return self
    def user_check(self,user, errors):
        if len(user)<5:
            errors.append('User Name must be at least 5 characters long')
            return self
    def zip_check(self,zip_code, errors):
        if zip_code < '00501' or zip_code >'99951':
            errors.append('Not a valid zip code.')
            return self
    def pass_check(self, password, repass, errors):
        if password!= repass:
            errors.append('Passwords do not match.Pease try again')
            return self
    def pass_val(self, password, errors):
        if len(password)<6:
            errors.append('Password not long enough. Password must be at least 6 characters')
            return self
    def create_user(self,data):
        hashed_pw=bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
        zip_code=data['zip'].zfill(5)
        self.create(f_name=data['f_name'].title(), l_name=data['l_name'].title(),u_name=data['u_name'].title(), email=data['email'].title(), password=hashed_pw, z_code=zip_code)
class User(models.Model):
    f_name=models.CharField(max_length=40)
    l_name=models.CharField(max_length=40)
    u_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=255)
    z_code=models.CharField(max_length=5)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

# Create your models here.
