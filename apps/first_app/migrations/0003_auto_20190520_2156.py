# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20190520_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
