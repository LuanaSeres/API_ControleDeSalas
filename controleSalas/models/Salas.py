from django.db import models

class EntidadeSala:
    def __init__(self, numeroSala, capacidade, descricao) -> None:
        self.numeroSala = numeroSala
        self.capacidade = capacidade
        self.descricao = descricao
    
    def __str__(self) -> str:
        return self.numeroSala

class EntidadeReserva:
    def __init__(self, numeroSala, dataInicio, dataFim, motivo) -> None:
        self.numeroSala = numeroSala
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.motivo = motivo

    def __str__(self) -> str:
        return self.numeroSala