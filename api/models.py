from django.db import models
import random

class BaseModel:
    _id = models.AutoField(primary_key=True, null=False, blank=False, auto_created=True)
    createdAt = models.DateField(auto_created=True)
    updatedAt = models.DateField()

def generateUserId():
    return  f"USER-{random.randint(1000, 9999)}"

# Create your models here.
class UpscUser(models.Model, BaseModel):
    userId = models.CharField(max_length=200, default=generateUserId)
    username = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(unique=True)