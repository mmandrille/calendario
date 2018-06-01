from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import *
from tinymce.models import HTMLField

#Create your models here.
class Evento(models.Model):
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
            "inicio": "{:%d/%m/%Y - %H:%M}".format(self.fecha_inicio),
            "duracion": ':'.join(str(self.fecha_fin-self.fecha_inicio).split(':')[:2]),
        }