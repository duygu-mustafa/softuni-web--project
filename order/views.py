from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import Address
from cart.cart import Cart
from order.forms import OrderCreateForm
from order.models import OrderItem


@login_required
def create_order(request):
    cart = Cart(request)
    profile = request.user.profile
    if request.method == 'GET':
        form = OrderCreateForm(initial={'profile_id': profile.id})
        context = {
            'form': form,
            'cart': cart,
            'user': request.user,
        }
        return render(request, 'order/create_order.html', context)
    else:
        form = OrderCreateForm(request.POST, initial={'profile_id': profile.id})
        if form.is_valid():
            order = form.save(commit=False)
            order.profile = request.user.profile
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                cart.clear()
                context = {
                    'order': order,
                }
                return render(request, 'order/created_thank_you.html', context)
        else:
            context = {
                'form': form,
                'cart': cart,
                'user': request.user,
            }
            return render(request, 'order/create_order.html', context)
