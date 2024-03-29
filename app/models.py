from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class historias (models.Model):
    nombre = models.CharField(max_length=40)
    resumen = models.CharField(max_length=100)
    protagonistas = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.nombre}"
    
class personajes (models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=40)
    habilidades = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="personajes")   
    def __str__(self):
        return f"{self.nombre}"

class mundos (models.Model):
    nombre = models.CharField(max_length=20)
    habitantes = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="mundos")

    def __str__(self):
        return f"{self.nombre}"
    
class objetos_magicos (models.Model):
    nombre = models.CharField(max_length=40)
    descripción = models.CharField(max_length=40)
    dueño = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.nombre}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return f"{self.user} {self.imagen}"
