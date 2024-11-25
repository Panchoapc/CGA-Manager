from django import forms
from production.models import ProductionEntry, Machine
from warehouse.models import Product

class ProductionForm(forms.ModelForm):
    # Custom field to combine product information
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        label="Product",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ProductionEntry  # This model should store production entries
        fields = ['machine', 'product', 'quantity']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizing product dropdown display with combined information
        self.fields['product'].queryset = Product.objects.all()
        self.fields['product'].label_from_instance = lambda obj: f"{obj.name} (x{obj.product_type.name}, {obj.brand.name})"
