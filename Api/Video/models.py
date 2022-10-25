from django.db import models

# Create your models here.

class Video(models.Model):

    titulo = models.CharField(max_length=50)
    description = models.TextField()
    fecha = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.titulo

    
