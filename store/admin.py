from django.contrib import admin
from .models import Product
from .models import Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')

# Register the VariationAdmin class for the Variation model in the Django admin site.
admin.site.register(Variation, VariationAdmin)
admin.site.register(Product, ProductAdmin)
