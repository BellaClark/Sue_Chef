# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-27 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_auto_20190527_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='total_steps',
            field=models.IntegerField(default=b'18'),
        ),
    ]