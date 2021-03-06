# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-21 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_switch_to_utf8mb4_columns'),
        ('topics', '0027_auto_20180516_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewspaperTopicPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=10, default=0, max_digits=16)),
                ('newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Newspaper')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Topic')),
            ],
            options={
                'ordering': ['topic__key', '-score'],
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='papers',
            field=models.ManyToManyField(through='topics.NewspaperTopicPair', to='news.Newspaper'),
        ),
        migrations.AddIndex(
            model_name='newspapertopicpair',
            index=models.Index(fields=['topic', '-score'], name='topics_news_topic_i_0e1992_idx'),
        ),
    ]
