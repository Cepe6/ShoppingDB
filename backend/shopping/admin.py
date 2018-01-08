# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, Product, Cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class NameAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'is_store']


admin.site.register(User, NameAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)