# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-25 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0032_articletopicrank_rank'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='topic',
            index=models.Index(fields=['key'], name='topics_topi_key_11822b_idx'),
        ),
    ]