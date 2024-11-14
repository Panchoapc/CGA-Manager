from django.db import models

class Role(models.Model):
    """Defines employee roles within the company."""
    name = models.CharField(max_length=50, unique=True)  # e.g., 'Manager', 'Technician'
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class BaseModel(models.Model):
    """Abstract base model with created and updated timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
