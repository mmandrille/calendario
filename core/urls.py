from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Personales
    url(r'^$', views.calendario, name='calendario'),

    #Web Services
    url('ws_eventos', views.ws_eventos, name='ws_eventos'),

    #TESTING PROYECT
    url('test/', views.test, name='test'),
]