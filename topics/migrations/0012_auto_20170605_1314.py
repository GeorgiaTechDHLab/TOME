# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20170605_1314'),
        ('topics', '0011_auto_20170605_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='corpus',
        ),
        migrations.AddField(
            model_name='yeartopicrank',
            name='corpus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Corpus'),
        ),
    ]
