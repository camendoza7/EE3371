from django.db import models

import datetime

from django.db import models
from django.utils import timezone

class Category(models.Model):
    text = models.CharField(max_length = 100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

class Description(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank = True)
    text = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(default = datetime.datetime.now())
