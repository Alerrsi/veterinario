from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nombre", "telefono", "correo", "direccion", "tipo"]



class ClienteSend(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "edad"]



class MascotaSend(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'
        



class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ["fecha", "motivo", "diagnostico", "tratamiento", "estado", "mascota", "veterinario"]



class ConsultaSend(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
        


class VetrinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ["nombre", "especialidad", "horarios", "estado"]



class VeterinarioSend(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'
        



class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ["id","nombre", "tipo", "dosis", "cantidad"]



class MedicamentoSend(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'
        




