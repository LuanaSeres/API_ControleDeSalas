from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from repository import RepositorioSalas
from ..serializers.SalasSerializers import SalasSerializers
import json

class DetalhesSalaView(View):
    def get(self, request, id):
        repository = RepositorioSalas()
        try:
            sala = repository.get_sala_by_id(id)
            serializer = SalasSerializers(sala)
            return JsonResponse(serializer.data)
        except RepositorioSalas.SalaNaoEncontradaException:
            return JsonResponse({'error': 'Sala de aula não encontrada'}, status=404)

    def put(self, request, id):
        repository = RepositorioSalas()
        try:
            sala = repository.get_sala_by_id(id)
            serializer = SalasSerializers(sala, data=json.loads(request.body))
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        except RepositorioSalas.SalaNaoEncontradaException:
            return JsonResponse({'error': 'Sala de aula não encontrada'}, status=404)
        
    def delete(self, request, id):
        repository = RepositorioSalas()
        try:
            repository.excluir_sala(id)
            return JsonResponse({'message': 'Sala de aula excluída com sucesso'})
        except RepositorioSalas.SalaNaoEncontradaException:
            return JsonResponse({'error': 'Sala de aula não encontrada'}, status=404)
