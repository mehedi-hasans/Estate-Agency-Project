from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField()