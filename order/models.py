from django.db import models
from django.db.models import CASCADE, DO_NOTHING

from accounts.models import Profile, Address
from shop.models import Item


class Order(models.Model):
    PENDING = 'PE'
    FULFILLED = 'FU'
    STATUS_CHOICES = [
        (PENDING, 'pending'),
        (FULFILLED, 'fulfilled'),
    ]

    profile = models.ForeignKey(Profile, on_delete=CASCADE)
    address = models.ForeignKey(Address, on_delete=DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='PE',
    )

    def __str__(self):
        return f'#{self.id} - order {self.profile.user.username}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=CASCADE, related_name='items')
    product = models.ForeignKey(Item, on_delete=CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
