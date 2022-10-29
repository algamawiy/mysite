from doctest import BLANKLINE_MARKER
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    slackUsername = models.CharField(max_length=100, blank=True, null=True)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField(max_length=300, blank=True, null=True)
    
    
    def __str__(self):
        return self.slackUsername
    