# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20190520_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.FloatField(),
        ),
    ]