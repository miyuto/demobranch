from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from rest_framework import serializers
from home.models import *
from .cart import Cart
# Create your views here.
def index(request):
    cateParents = TblCategory.objects.filter(cate_parent_id=0)
    featureItems = TblProduct.objects.filter(product_status=1)
    context = {
        'parents': cateParents,
        'products': featureItems
    }
    return render(request, 'home/index.html', context)

def detail(request, id):
    product = TblProduct.objects.get(product_id=id)
    cateParents = TblCategory.objects.filter(cate_parent_id=0)
    productImage = TblProductImage.objects.filter(product_id=id)
    context = {
        'product': product,
        'parents': cateParents,
        'productImage': productImage
    }
    return render(request, 'home/product-detail.html', context)

def add_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(TblProduct, product_id=id)
    form = request.POST
    cart.add(product=product, quantity=form['quantity'])

    return HttpResponseRedirect(reverse("cart"))

def get_cart(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'home/cart.html', context)

def login(request):

    return render(request, 'home/login.jinja2')