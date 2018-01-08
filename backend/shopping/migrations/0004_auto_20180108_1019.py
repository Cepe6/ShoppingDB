# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_auto_20180108_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='shopping.Cart'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='wish_list',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='wish_list', to='shopping.WishList'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='products', to='shopping.Product'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(related_name='wish_products', to='shopping.Product'),
        ),
    ]