from django.db import models
from django.contrib.auth.models import AbstractUser

class Pais(models.Model):
    nombre_Pais = models.CharField(max_length=100, unique=True, verbose_name="Nombre del País")

    def __str__(self):
        return self.nombre

class User(models.Model):
    usuario = models.CharField(max_length=100, unique=True, verbose_name="Nombre del País")

    def __str__(self):
        return self.nombre



    

class UsuarioBautismo(models.Model):
     # Campos numéricos
    libro = models.PositiveIntegerField()
    folio = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    fecha_bautismo = models.DateField()
   
    
    lugar_nacimiento =  models.CharField(max_length=100)
    nombreB = models.CharField(max_length=50)
    apellidosB = models.CharField(max_length=50)
    nombre_padre = models.CharField(max_length=50)
    nombre_madre = models.CharField(max_length=50)
    nombre_abuelo_paterno = models.CharField(max_length=50)
    nombre_abuela_paterna = models.CharField(max_length=50)
    nombre_abuelo_materno = models.CharField(max_length=50)
    nombre_abuela_materna = models.CharField(max_length=50)
    nombre_padrino = models.CharField(max_length=50)
    nombre_madrina = models.CharField(max_length=50)
    
    doy_fe = models.CharField(max_length=50)
   

    tipo_hijo = [
        ('legit', 'Legitimo'),
        ('adoptv', 'Adoptivo'),
        ('ilegit','Ilegítimo')
    ]
    tipo_hijo = models.CharField(max_length=15, choices=tipo_hijo)

    


