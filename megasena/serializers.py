from rest_framework import serializers
from megasena.models import SorteioMegaSena,NovoJogo

class SorteioMegaSenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SorteioMegaSena
        fields = '__all__'

class NovoJogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovoJogo
        fields = '__all__'

class NovoJogoDezenasSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovoJogo
        fields = ['dezenas']

class AcertosSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovoJogo
        fields = ['acertos']

