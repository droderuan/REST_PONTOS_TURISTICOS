from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacao = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer(many=False)

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao',
                  'aprovado', 'foto',
                  'atracoes', 'comentarios',
                  'avaliacao', 'endereco',) 
