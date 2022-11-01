from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
class Slackdata(models.Model):
    username = models.CharField(max_length=255,unique=True)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=255)
    typ = models.CharField(max_length=255,default='details')
    

    def __str__(self):
        return self.username