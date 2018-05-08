from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
#Import Personales
from .models import Evento

# Create your views here.
def calendario(request):
    eventos = Evento.objects.order_by('fecha_inicio')
    return render(request, 'home.html', { 'eventos': eventos, 'hoy' : datetime.now().strftime('%d/%m/%Y')})