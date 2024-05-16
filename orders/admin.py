# orders/admin.py

from django.contrib import admin
from .models import Order, OrderProduct

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone', 'city', 'address_line_1','quantity']  # Update list_display here

admin.site.register(Order, OrderAdmin)

