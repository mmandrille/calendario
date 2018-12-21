import json
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, timedelta
from django.db.models import Count
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
    #obtenemos los 10 Organismos mas usados
    ranking_organismos = Evento.objects.values("organismo").annotate(count=Count('organismo')).order_by("-count")[:5]
    #Obtenemos desde el sitio de organigrama todos los organismos > Ver models.py
    organismos = obtener_organismos()
    #lista_organismos= [organismo for organismo in organismos if organismo[0] == ranking_organismos[0]['organismo']]
    lista_organismos=   [organismo #SI, acabas de ver la listcompression mas loca de la historia xD
                        for organismo_ranking in [ranking['organismo']
                        for ranking in ranking_organismos]
                        for organismo in organismos
                        if organismo[0] == organismo_ranking]
    return render(request, 'home.html', {'organismos': lista_organismos, 'eventos': eventos, 'importantes': importantes, 'hoy' : datetime.now().strftime('%d/%m/%Y')})

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