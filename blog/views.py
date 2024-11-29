from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Blog, Mensagem
from django.forms.models import model_to_dict
from .forms import Mensagemform


def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, "index.html", context)

def post(request,post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
         "blog": Blog.objects.first(),
    }
    return render(request, "post.html", context)

def sobre(request):
    context = {
         "blog": Blog.objects.first(),
    }
    return render(request, "sobre.html", context)


def contato(request):    
    context = {
         "blog": Blog.objects.first(),
    }   

    if request.method == "POST":
        form = Mensagemform(request.POST)
        if form.is_valid():
            mensagem =Mensagem(
                nome = form.cleaned_data["nome"],
                email = form.cleaned_data["email"],
                telefone = form.cleaned_data["telefone"],
                mensagem = form.cleaned_data["mensagem"],
                cidade = form.cleaned_data["cidade"]
            )
            mensagem.save()

        return redirect('mensagem')
    else:
        context["form"] = Mensagemform()
        return render(request, "contato.html", context)
    
def mensagens (request):
    context = {
         "mensagens": Mensagem.objects.all(),
         "blog": Blog.objects.first(),
    }
    return render(request, "mensagens.html", context)
       

def editar_mensagens (request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    context = {
        "blog": Blog.objects.first(),
        "form": Mensagemform(initial=model_to_dict(mensagem))
    }

    return render(request, "contato.html", context)

def deletar_mensagens(request, mensagem_id):
    context = {
        "blog": Blog.objects.first(),
        "mensagem":Mensagem.objects.get(pk = mensagem_id)
    }

    if request.method == "POST":
        context['mensagem'].delete()
        return redirect('mensagens')
    else:
        return render(request, "delete_contato.html", context)
