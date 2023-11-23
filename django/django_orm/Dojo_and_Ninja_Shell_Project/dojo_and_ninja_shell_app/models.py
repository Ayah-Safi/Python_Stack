from django.db import models


class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255, null=True)


class Ninjas(models.Model):
    dojos = models.ForeignKey(Dojos, on_delete=models.CASCADE,related_name="ninja")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)