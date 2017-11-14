# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

<<<<<<< HEAD
<<<<<<< HEAD
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

class Post(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
=======
=======
>>>>>>> 6bdb327603555e2251c9f79e835715b409b14ee1
class User(models.Models):
    username = models.CharField(max_length = 20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class Image(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField()
    likes = models.IntegerField()
<<<<<<< HEAD
>>>>>>> 6bdb327603555e2251c9f79e835715b409b14ee1
=======
>>>>>>> 6bdb327603555e2251c9f79e835715b409b14ee1
