from django.shortcuts import render, redirect
from .models import Order, OrderProduct


def place_order(request):
    if request.method == 'POST':
        # Extract form data from the POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        quantity = request.POST.get('quantity')
        address_line_1 = request.POST.get('address_line_1')

        # Create a new Order instance with the form data
        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            city=city,
            quantity=quantity,
            address_line_1=address_line_1,
        )

        # Redirect to a success page or display a success message
        return redirect('order_success')

    # If the request method is not POST, render the form page
    return render(request, 'order_form.html')

def order_success(request):
    return render(request, 'order_success.html')

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    order_products = OrderProduct.objects.filter(order=order)
    return render(request, 'orders/order_detail.html', {'order': order, 'order_products': order_products})
