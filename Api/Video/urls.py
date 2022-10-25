from .views import ListVideo
from django.urls import path, re_path
from django.urls import re_path as url

#Las rutas de json se definen por url
#para ello importan el re_path 
#$: representa a los datos a mostrar de forma serializada
urlpatterns = [

    url(r'videos/$', ListVideo.as_view(), name='lista_video'),

]