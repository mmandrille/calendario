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