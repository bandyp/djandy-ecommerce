# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    about_me = models.TextField()
    nationality = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    
    def __unicode__(self):
        return self.title