from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem

def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_variation = []

    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)
            except Variation.DoesNotExist:
                pass

    cart_id = _cart_id(request)
    cart, created = Cart.objects.get_or_create(cart_id=cart_id)

    # Check if the item with the same variations already exists in the cart
    existing_cart_items = CartItem.objects.filter(product=product, cart=cart)
    for existing_cart_item in existing_cart_items:
        if set(existing_cart_item.variations.all()) == set(product_variation):
            # If the variations match, increase the quantity
            existing_cart_item.quantity += 1
            existing_cart_item.save()
            return redirect('cart')

    # If no matching CartItem found, create a new one with variations
    cart_item = CartItem.objects.create(
        product=product,
        quantity=1,
        cart=cart,
    )
    cart_item.variations.add(*product_variation)

    return redirect('cart')


def remove_cart(request, product_id, cart_item_id):
    cart_id = _cart_id(request)
    cart = get_object_or_404(Cart, cart_id=cart_id)
    product = get_object_or_404(Product, id=product_id)

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass

    return redirect('cart')

def remove_cart_item(request, product_id, cart_item_id):
    cart_id = _cart_id(request)
    cart = get_object_or_404(Cart, cart_id=cart_id)
    product = get_object_or_404(Product, id=product_id)

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart')

def cart(request):
    total = 0
    quantity = 0
    cart_items = None
    tax = 0
    grand_total = 0

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for item in cart_items:
            total += (item.product.price * item.quantity)
            quantity += item.quantity

        tax = (2 * total) / 100
        grand_total = total + tax
    except Cart.DoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)
