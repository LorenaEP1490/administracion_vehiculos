from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            "dominio",
            "marca",
            "modelo",
            "año",
            "version",
            "color",  # Asegúrate de que coincida con models.py
            "kilometros",
            "tipo_combustible",
            "transmision",
            "observaciones",
        ]
        widgets = {
            "dominio": forms.TextInput(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.NumberInput(attrs={"class": "form-control"}),
            "version": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(attrs={"class": "form-control"}),
            "kilometros": forms.NumberInput(attrs={"class": "form-control"}),
            "tipo_combustible": forms.Select(attrs={"class": "form-control"}),
            "transmision": forms.Select(attrs={"class": "form-control"}),
            "observaciones": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
