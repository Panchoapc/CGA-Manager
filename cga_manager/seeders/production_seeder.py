import os
import django
import sys

# Ensure the project root is in the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cga_manager.settings')
django.setup()

from production.models import Machine
from creation_helper_printer import print_creation_status

def seed_machines():
    machine_names = [
        "ACM",
        "Falu N1",
        "Falu N2",
        "Falu A1",
        "Falu Maxi",
        "Copos",
        "Prensado",
        "Absorbentes",
        "Packing",
        "Encajador",
        "Linea Cardas Antigua",
        "Linea Cardas RIETER"
    ]

    for name in machine_names:
        machine, created = Machine.objects.get_or_create(name=name)
        print_creation_status(machine, created)

if __name__ == "__main__":
    seed_machines()
