from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=30, null=False)
    subject = models.CharField(max_length=30, null=False)
    message = models.TextField()


    def __str__(self):
        return self.name