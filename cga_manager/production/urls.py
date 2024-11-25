from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_production, name='add_production'),
    path('success/', views.production_success, name='production_success'),
    path('machines/', views.MachineListView.as_view(), name='machine_list'),
    path('machines/create/', views.MachineCreateView.as_view(), name='machine_create'),
    path('machines/update/<int:pk>/', views.MachineUpdateView.as_view(), name='machine_update'),
    path('machines/delete/<int:pk>/', views.MachineDeleteView.as_view(), name='machine_delete'),
]