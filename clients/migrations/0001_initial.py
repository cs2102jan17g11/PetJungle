# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-28 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('animal', models.CharField(choices=[('CA', 'CAT'), ('DO', 'DOG'), ('RA', 'RABBIT')], max_length=2)),
                ('breed', models.CharField(max_length=20)),
            ],
        ),
    ]
