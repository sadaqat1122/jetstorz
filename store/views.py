from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category, ProductGallery
from carts.models import CartItem
from django.core.paginator import Paginator
from .models import SiteSettings

def store(request, category_slug=None):
    categories = None
    products = Product.objects.filter(is_available=True).order_by('id')

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=categories)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    paged_products = paginator.get_page(page_number)

    context = {
        'products': paged_products,
        'categories': categories,
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

    if keyword:
        products = Product.objects.filter(
            Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
        ).order_by('-created_date')

    context = {
        'products': products,
        'keyword': keyword,
        'product_count': products.count(),
    }
    return render(request, 'store/store.html', context)

def your_view(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'your_template.html', {'site_settings': site_settings})

def product_detail_view(request, product_id):
    single_product = get_object_or_404(Product, id=product_id)
    popular_products = Product.objects.filter(popularity='high')[:4]
    
    context = {
        'single_product': single_product,
        'popular_products': popular_products,
    }
    return render(request, 'product_detail.html', context)
def add_to_cart(request, product_id):
    # Your view logic
    return redirect('cart:add_to_cart', product_id=product_id)
    
def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    context = {
        'single_product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)