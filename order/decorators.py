from django.http import HttpResponse
from django.shortcuts import render

from cart.cart import Cart


def cart_items_required(func):
    def wrapper(request, *args, **kwargs):
        cart = Cart(request)
        if len(cart) == 0:
            return render(request, 'order/cart_empty.html')
        else:
            return func(request, *args, **kwargs)

    return wrapper
