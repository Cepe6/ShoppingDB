from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.users, name='users'), #Get, Post
    url(r'^users/(?P<user_id>[0-9]+)/$', views.user_info, name='user_info'), #Get, Put, Delete

    url(r'^users/buyers/$', views.buyers, name='buyers'), #Get
	url(r'^users/buyers/(?P<buyer_id>[0-9]+)/cart/$', views.cart, name='cart'),

    url(r'^users/stores/$', views.stores, name='stores'), #Get

    url(r'^products/$', views.products, name='products'), #Get, Post
    url(r'^products/(?P<product_id>[0-9]+)/$', views.product_info, name='product_info'), #Get, Put, Delete

]