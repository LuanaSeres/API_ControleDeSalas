from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import EntidadeSala
from ..serializers.SalasSerializers import SalaSerializer
from ..repository import RepositorioSalas

class CriarSalaView(APIView):
    def post(self, request, format=None):
        serializer = SalaSerializer(data=request.data)  # Passando os dados para o serializer
        if serializer.is_valid():
            serializer.save()
            # Instanciando a classe RepositorioSalas com o argumento collectionName
            repositorio = RepositorioSalas(collection='controlesala')
            repositorio.insert(serializer.data)  # Inserindo os dados no repositório
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self):
        return Response("ok")
