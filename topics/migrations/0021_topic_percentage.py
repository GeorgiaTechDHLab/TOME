# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0020_auto_20170630_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='percentage',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=10),
        ),
    ]
