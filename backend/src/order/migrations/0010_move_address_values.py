# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 12:40
from __future__ import unicode_literals

from django.db import migrations


def move_values_from_json_field_to_address_fields(apps, schema_editor):
    Order = apps.get_model("order", "Order")
    for order in Order.objects.all():
        print(order.address)
        order.street = order.address['street']
        order.building = order.address['building']
        order.apartment = order.address['apartment']
        order.floor = order.address['floor']
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_address_fields_added'),
    ]

    operations = [
        migrations.RunPython(move_values_from_json_field_to_address_fields)
    ]