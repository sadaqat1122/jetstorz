# orders/urls.py
from django.urls import path
from .views import place_order
from . import views

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),

    # Add more URL patterns as needed
]
