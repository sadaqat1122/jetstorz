from django.contrib import admin
from .models import Product, Variation, ProductGallery
from admin_thumbnails import thumbnail
from .models import SiteSettings

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

@thumbnail('image')  # Add this decorator to enable admin thumbnails
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')


class SiteSettingsAdmin(admin.ModelAdmin):
    # Customize the display of the SiteSettings model in the admin panel
    list_display = ['id', 'logo']
    search_fields = ['id']  # Add more fields if needed

# Register the models with their respective admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ProductGallery)


# Register the SiteSettings model with the custom admin class
admin.site.register(SiteSettings, SiteSettingsAdmin)
