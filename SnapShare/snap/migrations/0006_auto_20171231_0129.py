# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0005_auto_20171228_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
