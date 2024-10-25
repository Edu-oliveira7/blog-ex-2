from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "index.html", context)

def post(request,post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
    }
    return render(request, "post.html", context)

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    return render(request, "contato.html")