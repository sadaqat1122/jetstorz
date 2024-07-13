from django.shortcuts import render
from store.models import Product  # Adjust 'store' with your actual app name if different

def home(request):
    products = Product.objects.filter(is_available=True)

    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def whyus(request):
    return render(request, 'whyus.html')

def privacy_policy(request):
    return render(request, 'privacy.html')