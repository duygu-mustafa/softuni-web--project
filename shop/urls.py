from django.urls import path
from shop.views import index, about, list_items, item_details, list_earrings, list_rings, list_necklaces

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),

    path('products/', list_items, name='list items'),
    path('earrings/', list_earrings, name='list earrings'),
    path('rings/', list_rings, name='list rings'),
    path('necklaces/', list_necklaces, name='list necklaces'),

    path('product/<int:pk>', item_details, name='item details'),
]
