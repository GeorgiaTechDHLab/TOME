# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0015_auto_20170627_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='articles',
            field=models.ManyToManyField(through='topics.ArticleTopicRank', to='news.Article'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='words',
            field=models.ManyToManyField(through='topics.WordTopicRank', to='topics.Word'),
        ),
    ]
