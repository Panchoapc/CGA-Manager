from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Machine, ProductionEntry
from django.shortcuts import render, redirect
from production.forms import ProductionForm

@method_decorator(login_required, name='dispatch')
class MachineListView(ListView):
    model = Machine
    template_name = 'production/machine_list.html'
    context_object_name = 'machines'

@method_decorator(login_required, name='dispatch')
class MachineCreateView(CreateView):
    model = Machine
    fields = ['name']  # Customize fields as needed
    template_name = 'production/machine_form.html'
    success_url = reverse_lazy('machine_list')

@method_decorator(login_required, name='dispatch')
class MachineUpdateView(UpdateView):
    model = Machine
    fields = ['name']
    template_name = 'production/machine_form.html'
    success_url = reverse_lazy('machine_list')

@method_decorator(login_required, name='dispatch')
class MachineDeleteView(DeleteView):
    model = Machine
    template_name = 'production/machine_confirm_delete.html'
    success_url = reverse_lazy('machine_list')

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

@login_required
def production_success(request):
    return render(request, 'production/success.html')

@login_required
def working_machines_view(request):
    working_machines = Machine.objects.filter(is_working=True)  # Assuming an `is_working` field in Machine
    return render(request, 'production/working_machines.html', {'working_machines': working_machines})

@login_required
def past_production_view(request):
    past_productions = ProductionEntry.objects.order_by('-created_at')[:50]  # Show the latest 50 records
    return render(request, 'production/past_productions.html', {'past_productions': past_productions})