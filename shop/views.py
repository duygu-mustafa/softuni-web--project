from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from shop.models import Item, Favorite


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
        'is_in_user_fav': item.favorite_set.filter(user_id=request.user.profile.id).exists(),
    }
    return render(request, 'shop/items_details.html', context)


@login_required
def add_item_to_favorites(request, pk):
    fav = Favorite.objects.filter(user_id=request.user.profile.id, item_id=pk).first()
    if fav:
        fav.delete()
    else:
        item = Item.objects.get(pk=pk)
        fav = Favorite(test=str(pk), user=request.user.profile)
        fav.item = item
        fav.save()
    return redirect('item details', pk=pk)
