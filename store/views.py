from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category, ProductGallery
from carts.models import CartItem
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import SiteSettings

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.filter(is_available=True).order_by('id')

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    paged_products = paginator.get_page(page_number)

    context = {
        'products': paged_products,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=request.session.get('cart_id'), product=single_product).exists()

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    products = Product.objects.none()
    product_count = 0
    single_product = None

    if keyword:
        products = Product.objects.filter(
            Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
        ).order_by('-created_date')
        product_count = products.count()

        # Retrieve the first product object from the queryset
        if products.exists():
            single_product = products.first()

            # Fetch product gallery for the first product
            product_gallery = ProductGallery.objects.filter(product_id=single_product.id)
            context = {
                'single_product': single_product,
                'product_gallery': product_gallery,
                'in_cart': False,  # Replace this with logic to determine if the product is in the cart
                'orderproduct': None,  # Replace this with logic to retrieve the user's order history
                'reviews': None,  # Replace this with logic to retrieve product reviews
            }

    context = {
        'products': products,
        'keyword': keyword,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def your_view(request):
    # Fetch the site settings including the logo image
    site_settings = SiteSettings.objects.first()

    # Pass the logo image data to the template context
    return render(request, 'your_template.html', {'site_settings': site_settings})

