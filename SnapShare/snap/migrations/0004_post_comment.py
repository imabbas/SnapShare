# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0003_auto_20171222_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.CharField(default='', max_length=100),
        ),
    ]
