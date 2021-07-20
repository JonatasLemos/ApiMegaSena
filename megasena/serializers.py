from rest_framework import serializers
from megasena.models import SorteioMegaSena,NovoJogo

class SorteioMegaSenaSerializer(serializers.ModelSerializer):
    """Serializador para o modelo do ultimo sorteio da megasena"""
    class Meta:
        model = SorteioMegaSena
        fields = '__all__'

class NovoJogoSerializer(serializers.ModelSerializer):
    """Serializador para o modelo NovoJogo"""
    class Meta:
        model = NovoJogo
        fields = '__all__'

class NovoJogoDezenasSerializer(serializers.ModelSerializer):
    """Serializador para o modelo NovoJogo usando só o campo dezenas"""
    class Meta:
        model = NovoJogo
        fields = ['dezenas']

class AcertosSerializer(serializers.ModelSerializer):
    """Serializador para o modelo NovoJogo usando só o campo acertos"""
    class Meta:
        model = NovoJogo
        fields = ['acertos']

