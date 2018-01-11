# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User, Cart, WishList, Product, Buyer, Store


#/users/

def get_users(): 
    users = User.objects.all()
    response = []
    for u in users:
        type = ""
        if u.is_store:
            type = "store"
        else:
            type = "buyer"
        response.append({
                    "id": u.id,
                    "name" : u.name,
                    "type" : type
                })
    return JsonResponse(response, safe = False)

def add_user(request):
    data = json.loads(request.body)
    type = 0
    if data["type"] == "store":
        type = 1

    new = User(name = data["name"], is_store = type)
    new.save()

    if type == 0:
        cart = Cart(id = new.id)
        cart.save()

        list = WishList(id = new.id)
        list.save()

        buyer = Buyer(id = new.id, cart = cart, wish_list = list)
        buyer.save()
    else:
        store = Store(id = new.id)
        store.save()

    return JsonResponse({"status" : "add"})



@csrf_exempt
def users(request):
    if request.method == "GET":
        return get_users()
    elif request.method == "POST":
        return add_user(request)

#/users/id/

def get_user_info(user_id):
    user = User.objects.get(id = user_id)
    if user.is_store:
        type = "store"
    else:
        type = "buyer"

    response = {
                    "name" : user.name,
                    "type" : type,
                }
    return JsonResponse(response, safe = False)

def update(request, user_id):
    new_info = json.loads(request.body)

    type = 0
    if new_info["type"] == "store":
        type = 1

    User.objects.filter(id = user_id).update(name = new_info["name"])
    User.objects.filter(id = user_id).update(is_store = type)    

    return JsonResponse({"status" : "update"})

def delete(user_id):
    User.objects.get(id = user_id).delete();
    return JsonResponse({"status" : "delete"})

@csrf_exempt
def user_info(request, user_id):
    if request.method == "GET":
        return get_user_info(user_id)
    elif request.method == "PUT":
        return update(request, user_id)
    elif request.method == "DELETE":
        return delete(user_id)

#/buyers/
def buyers(request):
    buyers = User.objects.filter(is_store = False)
    response = []
    for b in buyers:
        response.append({
                    "id": b.id,
                    "name" : b.name,
                })
    return JsonResponse(response, safe = False)

#/stores/
def stores(request):
    buyers = User.objects.filter(is_store = True)
    response = []
    for b in buyers:
        response.append({
                    "id": b.id,
                    "name" : b.name,
                })
    return JsonResponse(response, safe = False)




#/products/

def get_products(): 
    products = Product.objects.all()
    response = []
    for p in products:
        response.append({
                    "id": p.id,
                    "name" : p.name,
                    "category" : p.category
                })
    return JsonResponse(response, safe = False)

def add_products(request):
    data = json.loads(request.body)
    new = Product(name = data["name"], category = data["category"], price = data["price"], description = data["description"])
    new.save()
    return JsonResponse({"status" : "add"})

@csrf_exempt
def products(request):
    if request.method == "GET":
        return get_products()
    elif request.method == "POST":
        return add_products(request)



#/products/id/

def get_product_info(product_id):
    product = Product.objects.get(id = product_id)
  
    response = {
                    "name" : product.name,
                    "category" : product.category,
                    "price" : product.price,
                    "description" : product.description
                }
    return JsonResponse(response, safe = False)

def update(request, product_id):
    new_info = json.loads(request.body)

    Product.objects.filter(id = product_id).update(name = new_info["name"])
    Product.objects.filter(id = product_id).update(category = new_info["category"]) 
    Product.objects.filter(id = product_id).update(price = new_info["price"])
    Product.objects.filter(id = product_id).update(description = new_info["description"])   

    return JsonResponse({"status" : "update"})

def delete(product_id):
    Product.objects.get(id = product_id).delete();
    return JsonResponse({"status" : "delete"})

@csrf_exempt
def product_info(request, product_id):
    if request.method == "GET":
        return get_product_info(product_id)
    elif request.method == "PUT":
        return update(request, product_id)
    elif request.method == "DELETE":
        return delete(product_id)


#/users/buyers/id/cart/

def get_cart(buyer_id): 
    cart = Cart.objects.get(id = buyer_id)
    response = []
    for p in cart.products.all():
        response.append({
                    "id": p.id,
                    "name" : p.name,
                    "category" : p.category
                })
    return JsonResponse(response, safe = False)

def add_cart(request, buyer_id):
    data = json.loads(request.body)
    product = Product.objects.get(id = data["product_id"])
    
    cart = Cart.objects.get(id = buyer_id)
    cart.products.add(product)
    cart.save()
    return JsonResponse({"status" : "add"})

@csrf_exempt
def cart(request, buyer_id):
    if request.method == "GET":
        return get_cart(buyer_id)
    elif request.method == "PUT":
        return add_cart(request, buyer_id)




#/users/buyers/id/wish_list/

def get_wish_list(list_id): 
    list = WishList.objects.get(id = list_id)
    response = []
    for p in list.products.all():
        response.append({
                    "id": p.id,
                    "name" : p.name,
                    "category" : p.category
                })
    return JsonResponse(response, safe = False)

def add_wish_list(request, list_id):
    data = json.loads(request.body)
    product = Product.objects.get(id = data["product_id"])
    
    list = WishList.objects.get(id = list_id)
    list.products.add(product)
    list.save()
    return JsonResponse({"status" : "add"})

@csrf_exempt
def wish_list(request, list_id):
    if request.method == "GET":
        return get_wish_list(list_id)
    elif request.method == "PUT":
        return add_wish_list(request, list_id)