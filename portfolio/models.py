from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField( max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'portfolio/images/')
    urls = models.URLField(blank = True)

    def __str__(self):
        return self.title

class Contacts(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    subject = models.CharField(max_length = 50)
    message = models.TextField()

    def __str__(self):
        return self.email
