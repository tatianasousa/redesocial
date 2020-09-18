from django.shortcuts import render
from perfis.models import *

def index(request):
    return render(request, 'index.html')

def exibirUsuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'usuario.html', {"usuario":usuario})

def exibirPerfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', {"perfil":perfil})

def exibirTimeline(request, timeline_id):
    timeline = Timeline.objects.get(id=timeline_id)
    return render(request, 'timeline.html', {"timeline":timeline})

def exibirPostagem(request, postagem_id):
    postagem = Postagem.objects.get(id=postagem_id)
    return render(request, 'postagem.html', {"postagem":postagem})

def exibirComentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    return render(request, 'comentario.html', {"comentario":comentario})

def exibirReacao(request, reacao_id):
    reacao = Reacao.objects.get(id=reacao_id)
    return render(request, 'reacao.html', {"reacao":reacao})
