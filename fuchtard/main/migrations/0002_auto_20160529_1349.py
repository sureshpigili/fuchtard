# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Подзаголовок'),
        ),
    ]
