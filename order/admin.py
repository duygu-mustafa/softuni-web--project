from django.contrib import admin

# Register your models here.
from order.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'address', 'status')
    list_filter = ('status', 'profile')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'product_id', 'quantity', 'price')
    list_filter = ('order_id',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
