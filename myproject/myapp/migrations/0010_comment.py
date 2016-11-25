# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20161028_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]
