from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from production.forms import ProductionForm
from production.models import ProductionEntry

@login_required
def add_production(request):
    if request.method == "POST":
        form = ProductionForm(request.POST)
        if form.is_valid():
            production_entry = form.save(commit=False)
            production_entry.worker = request.user  # Assume the logged-in user is the worker
            production_entry.save()
            return redirect('production_success')
    else:
        form = ProductionForm()
    return render(request, 'production/add_production.html', {'form': form})

def production_success(request):
    return render(request, 'production/success.html')
