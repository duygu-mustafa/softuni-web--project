from django.shortcuts import render

from shop.models import Item


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def list_items(request):
    context = {
        'items': Item.objects.all(),
        'label': 'All products',
    }
    return render(request, 'shop/items_list.html', context)

def list_earrings(request):
    earrings = [i for i in Item.objects.all() if i.type == 'ER']
    context = {
        'items': earrings,
        'label': 'Earrings',
    }
    return render(request, 'shop/items_list.html', context)

def list_rings(request):
    rings = [i for i in Item.objects.all() if i.type == 'RI']
    context = {
        'items': rings,
        'label': 'Rings',
    }
    return render(request, 'shop/items_list.html', context)

def list_necklaces(request):
    necklaces = [i for i in Item.objects.all() if i.type == 'NL']
    context = {
        'items': necklaces,
        'label': 'Necklaces',
    }
    return render(request, 'shop/items_list.html', context)


def item_details(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'shop/items_details.html', context)
