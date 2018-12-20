import json
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, timedelta
#Import Personales
from .models import Evento
from core.api import obtener_organismos

# Create your views here.
def calendario(request, org_id=None):
    eventos = Evento.objects.filter(fecha_inicio__date=date.today()).order_by('fecha_inicio')
    importantes = Evento.objects.filter(importante=True, fecha_inicio__date__gt=date.today()).order_by('fecha_inicio')
    if org_id is not None:
        eventos = eventos.filter(organismo=org_id)
        importantes = importantes.filter(organismo=org_id)
    return render(request, 'home.html', { 'eventos': eventos, 'importantes': importantes, 'hoy' : datetime.now().strftime('%d/%m/%Y')})

def ws_eventos(request, org_id=None):
    eventos =  Evento.objects.filter(fecha_inicio__date=date.today())
    importantes = Evento.objects.filter(importante=True, fecha_inicio__date__gt=date.today())
    if org_id is not None:
        eventos = eventos.filter(organismo=org_id)
        importantes = importantes.filter(organismo=org_id)
    dict_eventos = [evento.as_dict() for evento in eventos]
    dict_importantes = [evento.as_dict() for evento in importantes]    
    return HttpResponse(json.dumps({"eventos": dict_eventos, 'importantes': dict_importantes}), content_type='application/json')

def test(request):
    return render(request, 'consumir_eventos.html', {})