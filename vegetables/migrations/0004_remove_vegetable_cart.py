# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vegetables', '0003_vegetable_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vegetable',
            name='cart',
        ),
    ]