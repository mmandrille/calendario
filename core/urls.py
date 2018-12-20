from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Personales
    url(r'^$', views.calendario, name='calendario'),
    path('org/<int:org_id>', views.calendario, name='calendario'),

    #Web Services
    url(r'ws_eventos$', views.ws_eventos, name='ws_eventos'),
    path('ws_eventos/org/<int:org_id>', views.ws_eventos, name='ws_eventos'),

    #TESTING PROYECT
    url('test/', views.test, name='test'),
]