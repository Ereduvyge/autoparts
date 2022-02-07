from django.conf import settings
from django.db import models
from django.utils import timezone


class Ad(models.Model):
    site = models.TextField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
