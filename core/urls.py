from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.calendario, name='calendario'),
]