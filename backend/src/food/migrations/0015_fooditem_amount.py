# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0014_fooditem_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='amount',
            field=models.CharField(blank=True, max_length=20, verbose_name='Количество'),
        ),
    ]