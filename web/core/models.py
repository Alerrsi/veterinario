from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField("nombre", max_length=65)
    telefono = models.CharField("telefono", max_length=9)
    correo = models.EmailField(max_length=256)
    direccion = models.CharField("direccion", max_length=100)


    TYPES = [
        ("regular", "regular"),
        ("premium", "premium")
    ]

    tipo = models.CharField("tipo CLiente", choices=TYPES, max_length=7)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "clientes"
    
class Mascota(models.Model):
    nombre = models.CharField("nombre", max_length=65)
    especie = models.CharField("especie", max_length=65)
    raza = models.CharField("raza", max_length=65)
    edad = models.IntegerField("edad")
    peso = models.FloatField("edad")

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "mascotas"


class Veterinario(models.Model):
    nombre = models.CharField("nombre", max_length=65)
    especialidad = models.CharField("especialidad", max_length=100)
    horarios = models.CharField("horarios", max_length=100)
    ESTADOS = [
        ("Disponible", "disponible"),
        ("Ocupado", "ocupado"),
    ]
    estado = models.CharField("estadio", max_length=11, choices=ESTADOS)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "veterinarios"



class Consulta(models.Model):
    fecha = models.DateField()
    motivo = models.TextField("motivo consulta")
    diagnostico = models.CharField("diagnostico", max_length=100)
    tratamiento = models.CharField("tratamiento", max_length=200)

    ESTADOS = [
        ("Finalizada", "finalizada"),
        ("Realizada", "realizada"),
    ]
    estado = models.CharField("estado", max_length=11, choices=ESTADOS)

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    
    class Meta:
        db_table = "consultas"




class Medicamento(models.Model):
    nombre = models.CharField("nombre", max_length=65)
    tipo = models.CharField("tipo", max_length=100)
    dosis = models.CharField("dosis", max_length=100)
    cantidad = models.IntegerField("stock")

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "medicamnentos"


    




    







