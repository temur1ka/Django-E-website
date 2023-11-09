import stripe

from django.db import models




class Contacts(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.TextField()

class Task(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


