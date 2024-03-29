from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import EntidadeSala
from ..serializers import SalaSerializer
from ..repository import RepositorioSalas

class CriarSalaView(APIView):
    def post(self, request, format=None):
        serializer = SalaSerializer(data=request.data)
        if serializer.is_valid():
            numero_sala = serializer.validated_data.get('numeroSala')
            capacidade = serializer.validated_data.get('capacidade')
            descricao = serializer.validated_data.get('descricao')

            # Instanciando a entidade de Sala
            sala = EntidadeSala(numeroSala=numero_sala, capacidade=capacidade, descricao=descricao)

            # Salvando a sala no banco de dados
            repositorio = RepositorioSalas(collectionName='salas')
            repositorio.insert(sala.__dict__)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
