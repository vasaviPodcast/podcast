from django.db import models
from datetime import datetime

# Create your models here.
class PodcastDetails(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    contributor = models.CharField(max_length=100)
    audio = models.CharField(max_length=500)
    coverImage = models.CharField(max_length=500)
    uploadedOn = models.DateTimeField(default=datetime.now())

class User(models.Model):
    user = models.TextField(default=None)