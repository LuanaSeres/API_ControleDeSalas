from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models.Salas import EntidadeSala, EntidadeReserva
from ..formReserva import ReservaForm

class ReservarSala(View):
    def reservar_sala(request, sala_id):
      # Obtém a sala específica com base no ID fornecido
      sala = get_object_or_404(EntidadeSala, id=sala_id)
      
      if request.method == 'POST':
          # Se a requisição for um POST, processa os dados do formulário
          form = ReservaForm(request.POST)
          if form.is_valid():
              # Se o formulário for válido, cria uma nova reserva associada à sala
              reserva = form.save(commit=False)
              reserva.numeroSala = sala
              reserva.save()
              return JsonResponse({'message': 'Reserva criada com sucesso!'}, status=201)
          else:
              # Se o formulário não for válido, retorna os erros de validação
              return JsonResponse(form.errors, status=400)
      else:
          # Se a requisição não for um POST, retorna um formulário vazio para reservar a sala
          form = ReservaForm()
      
      # Renderiza um template com o formulário de reserva
      return render(request, 'reservarSala.html', {'form': form})