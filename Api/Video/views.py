from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from Video.serializers import VideoSerializazer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video

class  ListVideo(APIView):
    
    def get(self, request):

        #Mostrar todos los objetos de Videos
        videos = Video.objects.all()

        #Llevar la data serializada a la hora de ejecutar la aplicacion many=True
        video__json = VideoSerializazer(videos, many=True)

        #data: registros 

        return Response(video__json.data)
