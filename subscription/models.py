from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=100, default="")
    surname = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=15)
    startDate = models.DateField()
    endDate = models.DateField()