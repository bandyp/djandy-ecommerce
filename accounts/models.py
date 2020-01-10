# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Profile(models.Model):
    """
    The users profile information
    """
    name = models.CharField(max_length=100)
    about_me = models.TextField()
    nationality = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    
    def __unicode__(self):
        return self.title