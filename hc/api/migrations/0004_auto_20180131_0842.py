# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180131_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='priority',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
