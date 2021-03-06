# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0021_topic_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletopicrank',
            name='score',
            field=models.DecimalField(decimal_places=10, max_digits=16),
        ),
        migrations.AlterField(
            model_name='topic',
            name='percentage',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='topic',
            name='score',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='wordtopicrank',
            name='score',
            field=models.DecimalField(decimal_places=10, max_digits=16),
        ),
        migrations.AlterField(
            model_name='yeartopicrank',
            name='score',
            field=models.DecimalField(decimal_places=10, max_digits=16),
        ),
    ]
