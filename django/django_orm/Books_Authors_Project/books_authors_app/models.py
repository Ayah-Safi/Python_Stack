from django.db import models
 
class Books(models.Model):
    tittle = models.CharField(max_length=255)
    desc = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Authors(models.Model):
    books = models.ManyToManyField(Books,related_name="authors")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null = True)



