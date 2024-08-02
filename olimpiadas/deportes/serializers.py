from rest_framework import serializers
from .models import (
    TribunalDeJusticia, ConsejoDirectivo, CoordinadorDeportivo, Promocion,
    TablaDePosiciones, ExCadete, EventoDeportivo, Participacion,
    Resultado
)

class TribunalDeJusticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TribunalDeJusticia
        fields = '__all__'

class ConsejoDirectivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsejoDirectivo
        fields = '__all__'

class CoordinadorDeportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinadorDeportivo
        fields = '__all__'

class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = '__all__'


class TablaDePosicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaDePosiciones
        fields = '__all__'

class ExCadeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExCadete
        fields = '__all__'

class EventoDeportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoDeportivo
        fields = '__all__'  

class ParticipacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participacion
        fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = '__all__'