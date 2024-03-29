from django.views import View
from django.shortcuts import get_object_or_404, render
from ..models.Salas import EntidadeSala, EntidadeReserva
from ..serializers.SalasSerializers import ReservaSerializer
from utils import determinar_horarios_disponiveis

class ListaHorariosDisponiveis(View):
    def get(self, request, sala_id):
        # Obter a sala específica com base no ID fornecido
        sala = get_object_or_404(EntidadeSala, id=sala_id)
        
        # Obter todas as reservas para a sala específica
        reservas = EntidadeReserva.objects.filter(numeroSala=sala)
        
        # Determinar os horários disponíveis com base nas reservas existentes
        horarios_disponiveis = determinar_horarios_disponiveis(reservas)
        
        # Renderizar um template com os horários disponíveis
        return render(request, "listarHorarios.html", {"horarios_disponiveis": horarios_disponiveis})
