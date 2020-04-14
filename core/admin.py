from django.contrib import admin
from .models import Item, orderItem, order

# Register your models here.

admin.site.register(Item)
admin.site.register(orderItem)
admin.site.register(order)
