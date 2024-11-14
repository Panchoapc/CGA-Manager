from django.db import models
from warehouse.models import Product, Brand
from core.models import BaseModel

class Customer(BaseModel):
    """Represents a customer who may request production for specific brands."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    brands = models.ManyToManyField(Brand, related_name='customers', blank=True)  # Brands that CGA produces for this customer

    def __str__(self):
        return self.name

class Order(BaseModel):
    """Records customer orders."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} for {self.customer.name}"

class OrderItem(BaseModel):
    """Details each product in an order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.order}"
