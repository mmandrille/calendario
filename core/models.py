from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
#Para api
import requests 
import json

#Funciones API
def obtener_organismos():
	r = requests.get('http://organigrama.jujuy.gob.ar/ws_org/')
	orgs = json.loads(r.text)['data']
	organismos = list()
	for org in orgs:
		organismos.append((org['id'],org['nombre']))
	return organismos

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
            "inicio": "{:%d/%m/%Y - %H:%M}".format(self.fecha_inicio),
            "duracion": ':'.join(str(self.fecha_fin-self.fecha_inicio).split(':')[:2]),
        }