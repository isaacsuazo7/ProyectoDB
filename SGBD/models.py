from django.db import models

class Empleado(models.Model):
    codigo=models.IntegerField()
    nameE=models.CharField(max_length=100)
    telefonoE=models.CharField(max_length=15)

    class Meta:
        db_table = "empleado"
    
    def __str__(self):
        return self.nameE

class Animal(models.Model):
    nameA=models.CharField(max_length=100)
    medio = models.CharField(max_length=15)
    empleado = models.ForeignKey("Empleado", on_delete=models.CASCADE)
    alimentacion = models.OneToOneField("Alimentacion", on_delete=models.CASCADE)

    class Meta:
        db_table = "animal"
    
    def __str__(self):
        return self.nameA


class Alimentacion(models.Model):
    codigo=models.IntegerField()
    Tipoalimentacion = models.CharField(max_length=20)

    class Meta:
        db_table = "alimentacion"

    def __str__(self):
        return self.Tipoalimentacion