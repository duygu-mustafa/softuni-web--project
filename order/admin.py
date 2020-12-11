from django.contrib import admin

# Register your models here.
from order.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'address', 'status')
    list_filter = ('status', 'profile')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
