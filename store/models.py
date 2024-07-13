# store/models.py

from django.db import models
from django.urls import reverse
from category.models import Category  # Assuming Category model is defined in category app

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=(
        ('emirates', 'Emirates'),
        ('quantity', 'Quantity'),
    ))
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.variation_value

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='photos/products', max_length=255)

    def __str__(self):
        return self.product.product_name + " Gallery"

    class Meta:
        verbose_name = 'Product Gallery'
        verbose_name_plural = 'Product Galleries'

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logo_images/')
    # Add other site settings fields as needed

    def __str__(self):
        return 'Site Settings'
def store_detail_view(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    related_products = Product.objects.filter(store=store).exclude(id=product.id)[:4]
    
    return render(request, 'store/store_detail.html', {'store': store, 'related_products': related_products})