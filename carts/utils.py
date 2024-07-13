# carts/utils.py

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
