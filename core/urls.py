from django.urls import path
from controleSalas.views.ListarSalas import ListaSalasDisponiveis
from controleSalas.views.detalheSala import DetalhesSalaView
from controleSalas.views.ViewCriarSala import CriarSalaView
from controleSalas.views.listarHorarios import ListaHorariosDisponiveis
from controleSalas.views.reservaSala import ReservarSala


urlpatterns = [
    path('api/salas/', ListaSalasDisponiveis.as_view()),
    path('api/salas/<id>/', DetalhesSalaView.as_view()),
    path('api/salas/criar/', CriarSalaView.as_view()),
    path('api/salas/<id>/atualizar/', DetalhesSalaView.as_view()),
    path('api/salas/<id>/excluir/', DetalhesSalaView.as_view()),
    path('api/salas/<id>/horarios/', ListaHorariosDisponiveis.as_view()),
    path('api/salas/<id>/reservar/', ReservarSala.as_view()),
    path('api/reservas/<id>/cancelar/', ReservarSala.as_view())
]
