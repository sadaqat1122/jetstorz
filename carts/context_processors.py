from .models import Cart, CartItem  # Importing Cart and CartItem models
from .views import _cart_id  # Importing _cart_id function from views

def counter(request):
    cart_count = 0  # Initializing cart_count variable
    
    # Check if 'admin' is not in request.path
    if 'admin' not in request.path:
        try:
            # Try to retrieve the Cart object using _cart_id function
            cart = Cart.objects.get(cart_id=_cart_id(request))
            
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # If authenticated, filter CartItem objects by user
                cart_items = CartItem.objects.filter(user=request.user)
            else:
                # If not authenticated, filter CartItem objects by cart
                cart_items = CartItem.objects.filter(cart=cart)
            
            # Calculate cart_count by summing the quantity of each CartItem
            cart_count = sum(cart_item.quantity for cart_item in cart_items)

        except Cart.DoesNotExist:
            pass  # If Cart does not exist, do nothing and cart_count remains 0

    # Return a dictionary with 'cart_count' as the key
    return {'cart_count': cart_count}
