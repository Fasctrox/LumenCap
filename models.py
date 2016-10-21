from __future__ import unicode_literals
from django.core.exceptions import ValidationError


from django.db import models

# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length = 20, blank=False)
    date = models.DateTimeField()
    text = models.TextField(blank = True)