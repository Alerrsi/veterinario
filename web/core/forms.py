from django import forms
from .models import Consulta, Veterinario,Mascota

class ConsultaForm(forms.ModelForm):
    veterinario = forms.ModelChoiceField(queryset=Veterinario.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}), label="Veterinario que atendio al paciente" )
    mascota = forms.ModelChoiceField(queryset=Mascota.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}), label="Mascota que recibio el tratamiento" )
    estado = forms.ChoiceField(choices=Consulta.ESTADOS)
    class Meta:
        model = Consulta
        fields = ["fecha","motivo", "diagnostico", "tratamiento", "estado", "mascota", "veterinario"]
        widgets = {
            'fecha': forms.DateInput(),
            'motivo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motivo de consulta'}),
            "diagnostico" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnostico del Medico'}),
            "tratamiento": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tratamiento aplicado por el Medico'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado de la consulta'}),
        }
