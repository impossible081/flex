from django.contrib import admin
from store.models import GuestCustomer, Item, OrderItem, Order, Category, ShippingAddress, Label

# Register your models here.
admin.site.register(GuestCustomer)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(ShippingAddress)
admin.site.register(Label)