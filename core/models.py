from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import *

#Create your models here.
class Evento(models.Model):
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField('Fecha del Evento', default=datetime.datetime.now())
    fecha_fin = models.DateTimeField('Fecha de fin del Evento', default=datetime.datetime.now())
    models.ForeignKey(User, on_delete=models.CASCADE)
    #ubicacion = ciudades? 
    def __str__(self):
        return self.nombre