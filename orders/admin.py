# orders/admin.py
from django.contrib import admin
from .models import Order, OrderProduct

class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'product_price', 'product_title', 'phone', 'city', 'address_line_1', 'created_at', 'quantity')

    def get_product_names(self, obj):
        # Retrieve product names from associated OrderProduct instances
        return ", ".join([op.product.name for op in obj.orderproduct_set.all()])

    get_product_names.short_description = 'Product Names'  # Set column title

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
