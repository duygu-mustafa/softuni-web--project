from django.urls import path

from cart.views import cart_detail, cart_add, cart_remove

urlpatterns = [
    path('', cart_detail, name='cart detail'),
    path('add/<int:pk>', cart_add, name='cart add'),
    path('remove/<int:pk>', cart_remove, name="cart remove"),
]