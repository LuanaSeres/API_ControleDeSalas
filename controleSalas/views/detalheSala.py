from django.views import View
from django.shortcuts import render
from repository import RepositorioSalas
from ..serializers.SalasSerializers import SalasSerializers

class DetalhesSalaView(View):
    def get(self, request, id):
        repository = RepositorioSalas()
        try:
            sala = repository.get_sala_by_id(id)
            serializer = SalasSerializers(sala)
            return render(request, "detalhesSala.html", {"sala": serializer.data})
        except RepositorioSalas.SalaNaoEncontradaException:
            return render(request, "salaNaoEncontrada.html")
