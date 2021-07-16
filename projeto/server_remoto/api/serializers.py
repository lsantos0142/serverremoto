from rest_framework import serializers
from server_remoto import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

    def create(self, validated_data):
        if models.Paciente.objects.filter(CPF__iexact=validated_data.get('CPF')):
            models.Paciente.objects.filter(CPF__iexact=validated_data.get('CPF')).update(**validated_data)
            paciente = models.Paciente.objects.filter(CPF__iexact=validated_data.get('CPF')).values()[0]
        elif models.Paciente.objects.filter(CNS__iexact=validated_data.get('CNS')):
            models.Paciente.objects.filter(CNS__iexact=validated_data.get('CNS')).update(**validated_data)
            paciente = models.Paciente.objects.filter(CPF__iexact=validated_data.get('CNS')).values()[0]
        else:
            paciente = models.Paciente.objects.create(**validated_data)
        return paciente

class ImunizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imunizacao
        fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lote
        fields = '__all__'

class PerdasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perdas
        fields = '__all__'