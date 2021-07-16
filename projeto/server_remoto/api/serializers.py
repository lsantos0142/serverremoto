from rest_framework import serializers
#from server_remoto import models
from .. import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'


class ImunizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imunizacao
        #fields = ['paciente_CPF', 'paciente_CNS', 'comorbidades', 'CRM_medico_resp',
        #          'num_BPC', 'dose', 'imunobiologico', 'lote', 'via_admn', 'local_admn',
        #          'vacinador', 'grupo', 'estrategia', 'data_aplic', 'data_apraz',
        #          'estado_1_dose', 'pais_1_dose','modificado']
        fields = '__all__'


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lote
        fields = '__all__'

class PerdasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perdas
        fields = '__all__'

class AtualizaServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtualizaServer
        fields = '__all__'