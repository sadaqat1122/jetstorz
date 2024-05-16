from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0

    if 'admin' not in request.path:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            
            if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user=request.user)
            else:
                cart_items = CartItem.objects.filter(cart=cart)
            
            cart_count = sum(cart_item.quantity for cart_item in cart_items)

        except Cart.DoesNotExist:
            pass

    return {'cart_count': cart_count}
