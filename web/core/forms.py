from django import forms
from .models import Consulta, Veterinario,Mascota

class ConsultaForm(forms.ModelForm):
    fecha = forms.DateTimeField(required=False)
    veterinario = forms.ModelChoiceField(queryset=Veterinario.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}), label="Veterinario que atendio al paciente" )
    mascota = forms.ModelChoiceField(queryset=Mascota.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}), label="Mascota que recibio el tratamiento" )
    estado = forms.ChoiceField(choices=Consulta.ESTADOS)
    class Meta:
        model = Consulta
        fields = ["fecha","motivo", "diagnostico", "tratamiento", "estado", "mascota", "veterinario"]
        widgets = {
            'motivo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motivo de consulta'}),
            "diagnostico" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnostico del Medico'}),
            "tratamiento": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tratamiento aplicado por el Medico'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado de la consulta'}),
        }

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "edad", "peso"]
        widgets = {
            'nombre' :forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre de la mascota"}),
            'especie' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Especie de la mascota'}),
            'raza' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Raza de la Mascota'}),
            'edad' : forms.NumberInput(attrs={'class' : 'form-control' , 'placeholder' : 'Edad de la Mascota'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso de la Mascota'}),
        }

class VeterinarioForm(forms.ModelForm):
    estado = forms.ChoiceField(choices=Veterinario.ESTADOS)
    class Meta:
        model = Veterinario
        fields = ["nombre", "especialidad", "horarios", "estado", ]
        widgets = {
            'nombre' :forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre del veterinario"}),
            'especialidad' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Especiealidad del Veterinario'}),
            'horarios' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Horarios Disponibles'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado del veterinario'}),
        }
