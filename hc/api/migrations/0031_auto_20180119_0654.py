# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-19 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20180118_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='nag_after',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='nag_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='check',
            name='alert_after',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
