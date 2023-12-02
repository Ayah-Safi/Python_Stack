from django.db import models
import re
from django.contrib.auth.hashers import check_password
import bcrypt

class Users_validation(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if Users.objects.filter(email=postData['email']).exists():
            errors['email'] = 'Email is already registered.'
        if len(postData['first_name']) < 2:
            errors["first_name"] = "user first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "user last name should be at least 2 characters"
        if len(postData['password']) <  8:
            errors['password']   = 'Password should be at least 8 characters'
        EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
        if not EMAILREGEX.match(postData['email']):
             errors['email'] = "Invalid email address!"
        if postData['confirm_password'] != postData['password']:
            errors['confirm_password'] = 'password is not the same'
        return errors
    def login_validator(self, postData):
        errors = {}
        try:
            user = Users.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Incorrect Password!"
        except Users.DoesNotExist:
            errors['email'] = "Email doesn't exist!"
        return errors

        

    
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    confirm_password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Users_validation()