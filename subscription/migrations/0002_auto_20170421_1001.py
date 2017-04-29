# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vegetable_subscription',
            name='sub',
        ),
        migrations.RemoveField(
            model_name='vegetable_subscription',
            name='veglist',
        ),
        migrations.AddField(
            model_name='subscription_vegetablelist',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subscription.Subscription'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='sub_type',
            field=models.CharField(choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Vegetable_Subscription',
        ),
    ]