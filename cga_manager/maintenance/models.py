from django.db import models
from production.models import Machine
from human_resources.models import Employee
from core.models import BaseModel

class ScheduledMaintenance(BaseModel):
    """Represents planned maintenance for machines."""
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='scheduled_maintenance')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Scheduled maintenance for {self.machine.name} on {self.date}"

class MaintenanceRecord(BaseModel):
    """Logs maintenance activities on machines."""
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='maintenance_records')
    performed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='maintenance')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Maintenance on {self.machine.name} by {self.performed_by} on {self.date}"
