# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 05:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WinRemote', '0005_auto_20170306_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 7, 5, 15, 27, 295000, tzinfo=utc)),
        ),
    ]
