from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from repository import RepositorioSalas
from ..serializers.SalasSerializers import SalaSerializer

class ListaSalasDisponiveis(View):
    def get(self, request):
        repository = RepositorioSalas(collectionName='nome_da_sua_colecao')
        
        salas_disponiveis = repository.getAll()
        
        serializer = SalaSerializer(salas_disponiveis, many=True)
        
        if serializer.is_valid():
            salas_serializadas = serializer.data
            return render(request, "listaSalas.html", {"salas": salas_serializadas})
        else:
            print(serializer.errors)
            return HttpResponse("Erro ao obter as salas disponíveis", status=500)
