from django.db import models

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=255)
    quantity = models.CharField(max_length=50)  # Ensure this is appropriate for your requirements
    created_at = models.DateTimeField(auto_now_add=True)
    product_title = models.CharField(max_length=255)  # Assuming a CharField for product title
    product_price = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming a DecimalField for price


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
   # product_name = models.CharField(max_length=100)
    #price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.CharField(max_length=50)  # Ensure this is appropriate for your requirements


    def __str__(self):
        return f"{self.product_name} - Quantity: {self.quantity}"
