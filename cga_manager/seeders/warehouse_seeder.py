import os
import django
import sys

# Ensure the project root is in the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cga_manager.settings')
django.setup()

from warehouse.models import Brand, Product, ProductType
from creation_helper_printer import print_creation_status

def seed_warehouse():
    # Create Brand
    swiss_beauty, created = Brand.objects.get_or_create(name="Swiss Beauty")
    print_creation_status("Brand 'Swiss Beauty'", created)

    # Create Product Types
    product_type_80, created = ProductType.objects.get_or_create(name="80", defaults={"description": "80 units per package"})
    print_creation_status("Product type '80'", created)

    product_type_100, created = ProductType.objects.get_or_create(name="100", defaults={"description": "100 units per package"})
    print_creation_status("Product type '100'", created)

    # Create Products
    petalo_simple, created = Product.objects.get_or_create(
        name="Petalo simple",
        sku="PS80",
        brand=swiss_beauty,
        product_type=product_type_80,
        defaults={"description": "Petalo simple 80-pack"}
    )
    print_creation_status("Product 'Petalo simple'", created)

    copos, created = Product.objects.get_or_create(
        name="Copos",
        sku="CP100",
        brand=swiss_beauty,
        product_type=product_type_100,
        defaults={"description": "Copos 100-pack"}
    )
    print_creation_status("Product 'Copos'", created)

if __name__ == "__main__":
    seed_warehouse()
