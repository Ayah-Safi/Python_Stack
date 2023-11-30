from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
     def basic_validator(self, postData):
        errors = {}
        print(errors)
        if len(postData['title']) < 2 :
            errors["title"] = "Tv title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Tv network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Tv description should be at least 10 characters"
        if datetime.strptime(postData['date'],"%Y-%m-%d") > datetime.today():
            errors["date"]= "This date is in the future!, Please enter a date in the past. Thanks"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()

