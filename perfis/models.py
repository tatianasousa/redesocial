from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)
    data_nascimento = models.DateField()

class Perfil(models.Model):
    nome = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='perfis')
    contatos = models.ManyToManyField("self")

    def __str__(self):
        return self.nome

class Timeline(models.Model):
    perfil = models.OneToOneField(Perfil, related_name='timelines', on_delete=models.CASCADE)

class Postagem(models.Model):
    texto = models.CharField(max_length=50)
    data = models.DateField()
    timeline = models.OneToOneField(Timeline, related_name='postagens', on_delete=models.CASCADE)

class Comentario(models.Model):
    texto = models.CharField(max_length=200)
    data = models.DateField()
    perfil = models.OneToOneField(Perfil, related_name='comentarios_perfil', on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, related_name='comentarios_postagem', on_delete=models.CASCADE)

class TipoReacao(models.Model):
    tipo_reacao = models.CharField(max_length=50)

class Reacao(models.Model):
    tipo = models.OneToOneField(TipoReacao, related_name='reacao', on_delete=models.CASCADE)
    data = models.DateField()
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='reacoes')
    timeline = models.ForeignKey(Timeline, related_name='reacoes_timeline', on_delete=models.CASCADE)
    peso = models.IntegerField()  
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='perfis_reacao')


