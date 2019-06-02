# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('amount', models.IntegerField()),
                ('measurement', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('time_to_cook', models.IntegerField()),
                ('servings', models.IntegerField()),
                ('cals_per_serv', models.IntegerField()),
                ('main_photo', models.ImageField(upload_to=b'recipe_photos/')),
                ('recipe_photo', models.ImageField(upload_to=b'recipe_photos/')),
                ('ingredients', models.ManyToManyField(related_name='recipes', to='first_app.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.TextField()),
                ('set_timer_amount', models.FloatField(default=b'0.0')),
                ('photo', models.ImageField(upload_to=b'steps/')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('amount', models.IntegerField()),
                ('measurement', models.CharField(max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.ManyToManyField(related_name='recipes', to='first_app.Step'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tools',
            field=models.ManyToManyField(related_name='recipes', to='first_app.Tool'),
        ),
    ]
