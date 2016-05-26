# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 12:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20160501_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Содержимое корзины', 'verbose_name_plural': 'Содержимое корзины'},
        ),
        migrations.AlterModelOptions(
            name='gift',
            options={'ordering': ('requirement',), 'verbose_name': 'Подарок', 'verbose_name_plural': 'Подарки'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='order',
            name='order_created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 26, 12, 48, 0, 875093, tzinfo=utc), verbose_name='Заказ создан'),
            preserve_default=False,
        ),
    ]
