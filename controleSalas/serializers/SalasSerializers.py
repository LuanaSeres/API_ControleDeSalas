from rest_framework import serializers

class SalaSerializer(serializers.Serializer):
    numeroSala = serializers.FloatField()
    capacidade = serializers.FloatField()
    descricao = serializers.CharField()


class ReservaSerializer(serializers.Serializer):
    numeroSala = serializers.FloatField()
    dataInicio = serializers.DateTimeField()
    dataFim = serializers.DateTimeField()
    motivo = serializers.CharField()
