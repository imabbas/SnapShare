# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Models):
    username = models.CharField(max_length = 20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class Image(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField()
    likes = models.IntegerField()
