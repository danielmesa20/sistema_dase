from django.db import models

# Create your models here.

# class beca_excelencia(models.Model):
#     nombre = models.CharField(max_length=100, null=True)
#     cedula = models.IntegerField()
#     carrera = models.CharField(max_length=100, null=True)
#     tipo_beneficio = models.CharField(max_length=100, null=True)
#     porcentaje = models.IntegerField(null=True)
#     aportante_fondo_becas = models.CharField(max_length=200, null=True)
#     observaciones = models.CharField(max_length=500, null=True)


class estudiantes(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_beneficio = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)


class materias(models.Model):
    id = models.AutoField(primary_key=True)
    cedula_fk = models.ForeignKey(estudiantes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    inscrita = models.BooleanField()
    trimestre = models.CharField(max_length=100)


class indices(models.Model):
    id = models.AutoField(primary_key=True)
    cedula_fk = models.ForeignKey(estudiantes, on_delete=models.CASCADE)
    trimestre = models.CharField(max_length=100)
    iaa = models.IntegerField()
    iap = models.IntegerField()


# Relacion many to many: aportantes con estudiantes

# class aportantes(models.Model):
#     id = models.AutoField(primary_key=True)  # auto incremental
#     cedula_fk = models.ManyToManyField(estudiantes)  # crea una nueva tabla
#     nombre_aportante = models.CharField(max_length=100)
#     trimestre = models.CharField(max_length=10)

#     class Meta:
#         db_table = 'aportantes'  # Nombre que tendra la tabla en la base de datos


# # Relacion one to many: estudiante con observaciones
# class observaciones(models.Model):
#     id = models.AutoField(primary_key=True)
#     cedula_fk = models.ForeignKey(estudiantes, on_delete=models.CASCADE)
#     observacion = models.CharField(max_length=300)
#     trimestre = models.CharField(max_length=10)

# # Relacion one to one usa OnetoOneField
