from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length= 140)
    subtitulo = models.CharField(max_length = 140, blank =True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField(max_length =2000)
    capa = models.ImageField(blank=True)
    

    def __str__(self):
        return self.titulo

