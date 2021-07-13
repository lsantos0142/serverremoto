from rest_framework import serializers
from server_remoto import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

class ImunizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imunizacao
        fields = '__all__'