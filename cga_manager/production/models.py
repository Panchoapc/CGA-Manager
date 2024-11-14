from django.db import models
from warehouse.models import Product
from human_resources.models import Employee
from core.models import BaseModel

class Shift(models.Model):
    """Defines a general shift type."""
    name = models.CharField(max_length=50)  # e.g., 'Morning', 'Evening'
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class DailyShift(models.Model):
    """Represents a specific shift occurrence on a given day."""
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='daily_shifts')
    date = models.DateField()

    def __str__(self):
        return f"{self.shift.name} on {self.date}"

class Machine(models.Model):
    """Represents a machine in the factory."""
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='machines')

    def __str__(self):
        return self.name

class MachineUsage(models.Model):
    """Tracks machine usage during specific shifts with employee assignments and production yield."""
    daily_shift = models.ForeignKey(DailyShift, on_delete=models.CASCADE, related_name='machine_usages')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='usages')
    employees = models.ManyToManyField(Employee, related_name='machine_usages')
    yield_amount = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., units produced

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['daily_shift', 'machine'], name='unique_dailyshift_machine'),
            models.CheckConstraint(check=models.Q(yield_amount__gte=0), name='positive_yield_amount')
        ]
        ordering = ['daily_shift__date']

    def __str__(self):
        return f"{self.machine.name} on {self.daily_shift} - Yield: {self.yield_amount}"
    
class ProductionEntry(models.Model):
    worker = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="production_entries")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.worker} - {self.machine} - {self.product} - {self.quantity}"
