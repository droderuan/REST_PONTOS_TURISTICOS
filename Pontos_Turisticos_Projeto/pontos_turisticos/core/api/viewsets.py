from rest_framework import request
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
# formas de autenticação
from rest_framework.permissions import (DjangoModelPermissions,
                                        IsAdminUser,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    # solicita que o usuário esteja autenticado
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', '^endereco__linha1')
    # lookup_field troca a busca que ao inves de usar a ID (que é padrão),
    # usa o campo que eu específicar
    # deve ser um campo unico identificadora do recurso, pra n ocorrer 2
    # recursos ou mais na mesma busca
    lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        
        if nome:
            # __iexact no final faz com que n seja case sensitive
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    # GET para todos os recursos
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # POST
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # DELETE
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # GET num recurso específico
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    # PUT
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # PATCH
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
    
    # detail = True ele passa a pk, caso contrário será uma action do endpoint
    @action(methods=['get'], detail=True)  
    def denunciar(self, request, pk=None):
        return Response({"foi": 1})

    @action(methods=['get'], detail=False)
    def teste(self, request):
        return Response({"foi o teste": 34})
