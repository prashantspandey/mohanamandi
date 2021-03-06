# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 06:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vegetableOrder', '0009_vegetable_order_orderdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vegetable_order',
            name='orderveg',
        ),
        migrations.AddField(
            model_name='vegetable_order',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='vegetable_order',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vegetable_order',
            name='orderdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 22, 6, 58, 4, 314886, tzinfo=utc)),
        ),
    ]
