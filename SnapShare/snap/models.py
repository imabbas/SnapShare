# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Post(models.Model):
    image = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comment = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("snap:detail", (), kwargs={"pk": self.pk})

    def __str__(self):
        return self.comment
