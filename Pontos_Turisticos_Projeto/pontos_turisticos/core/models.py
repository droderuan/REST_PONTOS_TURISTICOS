from django.db import models
from django.db.models.fields.files import ImageField

from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos',
                             blank=True,
                             null=True)
    
    def __str__(self):
        return self.nome
