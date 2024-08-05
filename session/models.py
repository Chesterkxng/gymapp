from django.db import models
from datetime import datetime
from utils.utils import currentTime


# package table for sessions
class Package(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    amount = models.IntegerField()

# Session tables
class Session(models.Model):
    name = models.CharField(max_length=100, default="")
    surname = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=15)
    date = models.DateField(default=datetime.now().date())
    hour = models.TimeField(default=currentTime)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)