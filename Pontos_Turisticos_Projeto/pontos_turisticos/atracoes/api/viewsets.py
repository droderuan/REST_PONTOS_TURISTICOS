from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

#filter individual
from django_filters.rest_framework import DjangoFilterBackend


class AtracaoViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #para o filter individual
    filter_backends = (DjangoFilterBackend)
    filter_fields = ('nome', 'descricao')