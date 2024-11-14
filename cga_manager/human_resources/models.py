from django.db import models
from core.models import BaseModel, Role

class Employee(BaseModel):
    """Represents an employee in the factory."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)  # Unique employee identifier
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ShiftAssignment(BaseModel):
    """Records employee assignments to shifts."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='shift_assignments')
    daily_shift = models.ForeignKey('production.DailyShift', on_delete=models.CASCADE, related_name='employee_assignments')

    def __str__(self):
        return f"{self.employee} assigned to {self.daily_shift}"
