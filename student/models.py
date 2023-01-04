from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.IntegerField()
    istrue = models.BooleanField(default=True)
