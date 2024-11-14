from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel, Role

class Employee(AbstractUser):
    """Custom user model using RUT as the unique identifier for login."""
    username = None  # Remove the default username field
    rut = models.CharField(max_length=10, unique=True)  # Unique identifier
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='employees')

    USERNAME_FIELD = 'rut'  # Set RUT as the username field for authentication
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']  # Fields required when creating a user

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role.name}"

class ShiftAssignment(BaseModel):
    """Records employee assignments to shifts."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='shift_assignments')
    daily_shift = models.ForeignKey('production.DailyShift', on_delete=models.CASCADE, related_name='employee_assignments')

    def __str__(self):
        return f"{self.employee} assigned to {self.daily_shift}"
