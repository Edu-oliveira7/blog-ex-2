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
    
class Blog(models.Model):
    nome = models.CharField(max_length=100)
    subnome = models.CharField(max_length=100, blank = True)
    descricao = models.TextField(max_length=2000)
    capa = models.ImageField()
    instagram = models.URLField(blank = True)
    facebook = models.URLField( blank = True)
    github = models.URLField( blank = True)
    autores = models.ManyToManyField(User)

    def __str__(self):
        return self.nome
    

class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    mensagem = models.TextField(max_length=1000)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.email}"    

