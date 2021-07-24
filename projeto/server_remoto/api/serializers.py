from rest_framework import serializers
from ..models import Imunizacao, Imunobiologico, Paciente, Lote, AtualizaServer
from django.contrib.auth.models import User
#from server_remoto import models
from .. import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'


class ImunizacaoSerializer(serializers.ModelSerializer):
    paciente_CPF = serializers.SerializerMethodField()
    paciente_CNS = serializers.SerializerMethodField()
    imunobiologico = serializers.SerializerMethodField() 
    lote = serializers.SerializerMethodField() 
    vacinador = serializers.SerializerMethodField()

    class Meta:
        model = models.Imunizacao
        fields = ['id','paciente_CPF', 'paciente_CNS', 'comorbidades', 'CRM_medico_resp',
                  'num_BPC', 'dose', 'imunobiologico', 'lote', 'via_admn', 'local_admn',
                  'vacinador', 'grupo', 'estrategia', 'data_aplic', 'data_apraz',
                  'estado_1_dose', 'pais_1_dose'
                 ]
    
    def get_paciente_CPF(self, obj):
        #return 0
        return Paciente.objects.filter(id=obj.paciente_id).first().CPF

    def get_paciente_CNS(self, obj):
        #return 0
        return Paciente.objects.filter(id=obj.paciente_id).first().CNS

    def get_imunobiologico(self, obj):
        #return 0
        return Imunobiologico.objects.filter(id=obj.imunobiologico_id).first().imunobiologico
    
    def get_lote(self, obj):
        #return 0
        return Lote.objects.filter(id=obj.lote_id).first().lote
    
    def get_vacinador(self, obj):
        # print(User.objects.filter(id=obj['vacinador_id']).first())
        return User.objects.filter(id=obj.vacinador_id).first().username


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