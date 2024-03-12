from django.db import models
from django.contrib.auth.models import User
import uuid

class Coffee(models.Model):
    name= models.CharField(max_length=255)
    price= models.FloatField()
    quantity= models.IntegerField()
    image= models.CharField(max_length=2083)

