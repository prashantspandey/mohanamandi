# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_veg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='veg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetables.Vegetable'),
        ),
    ]
