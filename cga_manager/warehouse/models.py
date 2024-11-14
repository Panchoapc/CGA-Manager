from django.db import models
from core.models import BaseModel

class Brand(BaseModel):
    """Represents a brand, such as 'Swiss Beauty'."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ProductType(BaseModel):
    """Defines the type or format of a product, such as '80' (for 80 units per package)."""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    """Represents a product, linked to a brand and type."""
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} ({self.product_type.name}) - {self.brand.name}"

class StockItem(BaseModel):
    """Tracks inventory levels of products."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_items')
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=100)  # e.g., 'Warehouse A'

    def __str__(self):
        return f"{self.product.name} at {self.location} - {self.quantity} units"

class InventoryTransaction(BaseModel):
    """Logs transactions affecting stock levels."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transactions')
    change = models.IntegerField()  # Positive for addition, negative for subtraction
    reason = models.CharField(max_length=100)  # e.g., 'Production', 'Shipment'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.change} units of {self.product.name} for {self.reason}"
