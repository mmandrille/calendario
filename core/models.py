from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import *

#Create your models here.
class Evento(models.Model):
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField('Fecha del Evento')
    models.ForeignKey(User, on_delete=models.CASCADE)
    #ubicacion = ciudades? 
    pub_date = models.DateTimeField('Fecha de Publicacion', default=datetime.datetime.now())
    def __str__(self):
        return self.nombre