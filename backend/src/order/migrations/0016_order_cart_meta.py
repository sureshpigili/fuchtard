# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 11:34
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20170424_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]