# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160919_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='modelo',
            field=models.TextField(default='n60'),
            preserve_default=False,
        ),
    ]
