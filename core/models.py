from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User
#Import Modulos Extras
from tinymce.models import HTMLField
#Import propios
from core.api import obtener_organismos

#Create your models here.
class Evento(models.Model):
    organismo = models.PositiveIntegerField(choices= obtener_organismos(), default=0)
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = HTMLField()
    fecha_inicio = models.DateTimeField('Fecha del Evento', default=datetime.datetime.now)
    fecha_fin = models.DateTimeField('Fecha de fin del Evento', default=datetime.datetime.now)
    models.ForeignKey(User, on_delete=models.CASCADE)
    importante = models.BooleanField(default=False)
    #ubicacion = ciudades? 
    def __str__(self):
        return self.nombre + ' ' + str(self.fecha_inicio)
    def as_dict(self):
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "inicio": "{:%d/%m/%Y - %H:%M}".format(self.fecha_inicio),
            "duracion": ':'.join(str(self.fecha_fin-self.fecha_inicio).split(':')[:2]),
        }