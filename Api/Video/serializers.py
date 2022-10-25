from rest_framework import serializers
from .models import Video

class VideoSerializazer(serializers.ModelSerializer):

    class Meta:

        model = Video

        fields = ('id', 'titulo', 'descripcion')
