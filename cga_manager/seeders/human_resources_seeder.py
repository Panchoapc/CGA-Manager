import os
import django
import sys

# Ensure the project root is in the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cga_manager.settings')
django.setup()

from human_resources.models import Employee, Role
from creation_helper_printer import print_creation_status

def seed_employees():
    try:
        # Create Roles
        admin_role, created = Role.objects.get_or_create(name="Admin", defaults={"description": "System Administrator"})
        print_creation_status("Admin role", created)

        supervisor_role, created = Role.objects.get_or_create(name="Supervisor", defaults={"description": "Supervises workers and manages production processes"})
        print_creation_status("Supervisor role", created)

        worker_role, created = Role.objects.get_or_create(name="Worker", defaults={"description": "Standard employee with limited privileges"})
        print_creation_status("Worker role", created)

        # Create Employees using RUT as username
        admin_user, created = Employee.objects.get_or_create(
            rut="12345678-9",
            first_name="Francisco",
            last_name="Pieper",
            email="fapieper@miuandes.com", 
            role=admin_role
        )
        if created:
            admin_user.set_password("securepassword")
            admin_user.save()
        print_creation_status("Admin user Francisco Pieper", created)

        supervisor_user, created = Employee.objects.get_or_create(
            rut="98765432-1",
            first_name="Carlos",
            last_name="Gomez",
            email="cgomez@factory.com",
            role=supervisor_role
        )
        if created:
            supervisor_user.set_password("securepassword")
            supervisor_user.save()
        print_creation_status("Supervisor Carlos Gomez", created)

        worker1, created = Employee.objects.get_or_create(
            rut="11223344-5",
            first_name="Ana",
            last_name="Martinez",
            email="amartinez@factory.com",
            role=worker_role
        )
        if created:
            worker1.set_password("securepassword")
            worker1.save()
        print_creation_status("Worker Ana Martinez", created)

        worker2, created = Employee.objects.get_or_create(
            rut="22334455-6",
            first_name="Luis",
            last_name="Rodriguez",
            email="lrodriguez@factory.com",
            role=worker_role
        )
        if created:
            worker2.set_password("securepassword")
            worker2.save()
        print_creation_status("Worker Luis Rodriguez", created)
        
    except Exception as e:
        print("An error occurred during seeding:", e)

if __name__ == "__main__":
    seed_employees()
