from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from human_resources.models import Employee
from production.models import Machine, ProductionEntry
from warehouse.models import Product

@login_required
def dashboard(request):
    user = request.user
    context = {"user": user}

    # Common context data based on user roles
    if user.role.name == "Admin":
        # Admin-specific context
        context.update({
            "machines": Machine.objects.all(),
            "products": Product.objects.all(),
            "employees": Employee.objects.all(),
        })
        template_name = 'dashboards/admin_dashboard.html'

    elif user.role.name == "Supervisor":
        # Supervisor-specific context
        context.update({
            "employees": Employee.objects.filter(role__name="Worker"),
            "past_productions": ProductionEntry.objects.order_by('-created_at')[:50]  # Example to get recent production
        })
        template_name = 'dashboards/supervisor_dashboard.html'

    elif user.role.name == "Worker":
        # Worker-specific context
        context.update({
            "message": f"Hello, {user.first_name}!",
            "recent_productions": ProductionEntry.objects.filter(worker=user).order_by('-created_at')[:5],
        })
        template_name = 'dashboards/worker_dashboard.html'

    else:
        # Default fallback (if role is not recognized)
        template_name = 'homepage.html'

    return render(request, template_name, context)
