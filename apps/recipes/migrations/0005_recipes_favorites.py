# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161025_0658'),
        ('recipes', '0004_merge_20161027_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='favorites',
            field=models.ManyToManyField(related_name='favs', to='login.User'),
        ),
    ]
