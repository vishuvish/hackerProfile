# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-16 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20171016_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='hacker',
            name='problems_solved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hacker',
            name='ratings',
            field=models.IntegerField(default=0),
        ),
    ]
