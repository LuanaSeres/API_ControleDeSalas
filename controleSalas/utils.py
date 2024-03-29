from datetime import timedelta

def determinar_horarios_disponiveis(reservas):
    # Definir a duração mínima de uma reserva (em minutos)
    duracao_minima_reserva = 60
    
    # Definir o intervalo de tempo para verificar a disponibilidade (em minutos)
    intervalo_verificacao = 30
    
    # Inicializar uma lista para armazenar os horários disponíveis
    horarios_disponiveis = []
    
    # Iterar sobre cada reserva e verificar os horários disponíveis entre elas
    for i, reserva in enumerate(reservas):
        # Calcular o horário de início e fim da reserva atual
        inicio_reserva = reserva.dataInicio
        fim_reserva = reserva.dataFim
        
        # Verificar se há tempo disponível antes da primeira reserva
        if i == 0:
            inicio_disponivel = inicio_reserva - timedelta(minutes=duracao_minima_reserva)
            while inicio_disponivel + timedelta(minutes=duracao_minima_reserva) <= inicio_reserva:
                horarios_disponiveis.append(inicio_disponivel)
                inicio_disponivel += timedelta(minutes=intervalo_verificacao)
        
        # Verificar se há tempo disponível entre reservas consecutivas
        if i < len(reservas) - 1:
            proxima_reserva = reservas[i + 1]
            fim_disponivel = fim_reserva
            inicio_proxima_reserva = proxima_reserva.dataInicio
            while fim_disponivel + timedelta(minutes=duracao_minima_reserva) <= inicio_proxima_reserva:
                horarios_disponiveis.append(fim_disponivel)
                fim_disponivel += timedelta(minutes=intervalo_verificacao)
        
        # Verificar se há tempo disponível após a última reserva
        if i == len(reservas) - 1:
            fim_disponivel = fim_reserva
            while fim_disponivel + timedelta(minutes=duracao_minima_reserva) <= fim_reserva:
                horarios_disponiveis.append(fim_disponivel)
                fim_disponivel += timedelta(minutes=intervalo_verificacao)
    
    return horarios_disponiveis
