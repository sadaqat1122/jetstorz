from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def _get_or_create_cart(request):
    """
    Get or create a cart for the current user.
    """
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart = Cart.objects.create()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
    return Cart.objects.get(id=cart_id)

@login_required
def add_to_cart(request, product_id):
    """
    Add a product to the cart.
    """
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    product_variations = []

    if request.method == 'POST':
        for key, value in request.POST.items():
            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                product_variations.append(variation)
            except Variation.DoesNotExist:
                pass

    cart = _get_or_create_cart(request)

    for existing_cart_item in CartItem.objects.filter(product=product, user=user):
        if set(existing_cart_item.variations.all()) == set(product_variations):
            existing_cart_item.quantity += 1
            existing_cart_item.save()
            return redirect('cart')

    cart_item = CartItem.objects.create(
        product=product,
        quantity=1,
        user=user,
        cart=cart,
    )
    cart_item.variations.add(*product_variations)

    return redirect('cart')

@login_required
def remove_from_cart(request, product_id, cart_item_id):
    """
    Remove a quantity of a product from the cart.
    """
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, product=product, user=user, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

@login_required
def remove_cart_item(request, product_id, cart_item_id):
    """
    Remove a product from the cart.
    """
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, product=product, user=user, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

@login_required
def view_cart(request):
    """
    View the contents of the cart.
    """
    user = request.user
    cart_items = CartItem.objects.filter(user=user, is_active=True)
    total, quantity, tax, grand_total = calculate_totals(cart_items)

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)

def _cart_id(request):
    """
    Retrieve the cart ID from the session or create a new one if it doesn't exist.
    """
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart = Cart.objects.create()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
    return cart_id


@login_required
def checkout(request):
    """
    Proceed to checkout.
    """
    user = request.user
    cart_items = CartItem.objects.filter(user=user, is_active=True)
    total, quantity, tax, grand_total = calculate_totals(cart_items)

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'orders/checkout.html', context)

def calculate_totals(cart_items):
    """
    Calculate total, quantity, tax, and grand total from cart items.
    """
    total = sum(item.product.price * item.quantity for item in cart_items)
    quantity = sum(item.quantity for item in cart_items)
    tax = (2 * total) / 100
    grand_total = total + tax
    return total, quantity, tax, grand_total
