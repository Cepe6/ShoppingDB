# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_auto_20180108_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='othername',
        ),
        migrations.RemoveField(
            model_name='user',
            name='somename',
        ),
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='shopping.Cart'),
        ),
        migrations.AddField(
            model_name='user',
            name='wish_list',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wish_list', to='shopping.WishList'),
        ),
    ]