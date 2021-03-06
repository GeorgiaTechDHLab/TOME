# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0006_auto_20170307_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTopicRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.DecimalField(decimal_places=5, max_digits=5)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ManyToManyField(through='topics.ArticleTopicRank', to='news.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WordTopicRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.DecimalField(decimal_places=5, max_digits=5)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Topic')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Word')),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='words',
            field=models.ManyToManyField(through='topics.WordTopicRank', to='topics.Word'),
        ),
        migrations.AddField(
            model_name='articletopicrank',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Topic'),
        ),
        migrations.AlterUniqueTogether(
            name='wordtopicrank',
            unique_together=set([('word', 'topic')]),
        ),
        migrations.AlterUniqueTogether(
            name='articletopicrank',
            unique_together=set([('article', 'topic')]),
        ),
    ]
