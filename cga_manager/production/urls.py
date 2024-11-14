from django.urls import path
from production import views

urlpatterns = [
    path('add/', views.add_production, name='add_production'),
    path('success/', views.production_success, name='production_success'),
]
