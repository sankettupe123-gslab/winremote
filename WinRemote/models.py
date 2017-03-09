from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class history(models.Model):
    command = models.CharField(max_length=300)
    output = models.CharField(max_length=300)
    ip = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now())