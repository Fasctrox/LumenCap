# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
