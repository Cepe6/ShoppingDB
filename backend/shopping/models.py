# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = 1
    price = models.FloatField()
    description = models.TextField() 


class Category(models.Model):
    name = models.CharField(max_length=200)


class WishList(models.Model):
    products = models.ManyToManyField(Product, related_name='wish_products')

class Cart(models.Model):
    products = models.ManyToManyField(Product, related_name='products')


class User(models.Model):
    name = models.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    is_store = models.BooleanField()
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='cart', null = True, blank=True)
    wish_list = models.OneToOneField(WishList, on_delete=models.CASCADE,  related_name='wish_list', null = True, blank=True)