# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vegetables', '0004_remove_vegetable_cart'),
        ('cart', '0002_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='veg',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='vegetables.Vegetable'),
            preserve_default=False,
        ),
    ]
