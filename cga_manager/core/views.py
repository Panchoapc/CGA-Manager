from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from human_resources.models import Employee
from production.models import Machine
from warehouse.models import Product

@login_required
def homepage(request):
    user = request.user  # Get the logged-in user

    # Check user's role and prepare content accordingly
    context = {"user": user}
    if user.role.name == "Admin":
        # Fetch all machines, products, and employees for Admin
        context["machines"] = Machine.objects.all()
        context["products"] = Product.objects.all()
        context["employees"] = Employee.objects.all()
    elif user.role.name == "Supervisor":
        # Display a welcome message and list of all workers
        context["employees"] = Employee.objects.filter(role__name="Worker")
    elif user.role.name == "Worker":
        # Display a simple welcome message for Workers
        context["message"] = f"Hello, {user.first_name}!"

    return render(request, 'homepage.html', context)
