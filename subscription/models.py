from django.db import models


# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    amount = models.IntegerField()

class Subscription(models.Model):
    name = models.CharField(max_length=100, default="")
    surname = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=15)
    startDate = models.DateField()
    duration = models.IntegerField(default=1)
    endDate = models.DateField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)