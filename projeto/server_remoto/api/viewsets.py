from ..models import Imunobiologico
from rest_framework import viewsets
from server_remoto import models
from server_remoto.api import serializers
from rest_framework.response import Response

from django.contrib.auth.models import User

class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PacienteSerializer
    queryset = models.Paciente.objects.all()
    def patch(self, request, *args, **kwargs):
        if models.Paciente.objects.filter(CPF__iexact=request.data.get('CPF')):
            paciente = models.Paciente.objects.filter(CPF__iexact=request.data.get('CPF'))[0]
        elif models.Paciente.objects.filter(CNS__iexact=request.data.get('CNS')):
            paciente = models.Paciente.objects.filter(CPF__iexact=request.data.get('CNS'))[0]
        else:
            paciente = models.Paciente.objects.create(**request.data)
        serializer = serializers.PacienteSerializer(instance=paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ImunizacaoViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.ImunizacaoSerializer
    queryset = models.Imunizacao.objects.all()
    def patch(self, request, *args, **kwargs):
        data = request.data
        paciente_pk = 0
        imunobiologico_pk = 0
        lote_pk = 0
        vacinador_pk = 0

        paciente_CPF = data.pop('paciente_CPF')
        paciente_CNS = data.pop('paciente_CNS')
        if paciente_CPF:
            paciente_pk = models.Paciente.objects.filter(CPF=paciente_CPF).first().id
        else:
            paciente_pk = models.Paciente.objects.filter(CNS=paciente_CNS).first().id

        imunobiologico = data.pop('imunobiologico')
        imunobiologico_pk = models.Imunobiologico.objects.filter(imunobiologico=imunobiologico).first().id

        lote = data.pop('lote')
        lote_pk = models.Lote.objects.filter(lote=lote).first().id # Corrigir aqui para levar em conta não somente o nome do lote como também o nome do imunobiológico

        vacinador = data.pop('vacinador')
        vacinador_pk = User.objects.filter(username=vacinador).first().id

        data['paciente'] = paciente_pk
        data['imunobiologico'] = imunobiologico_pk
        data['lote'] = lote_pk
        data['vacinador'] = vacinador_pk
        print(data)
        serializer = serializers.ImunizacaoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class LoteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LoteSerializer
    queryset = models.Lote.objects.all()

class PerdasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PerdasSerializer
    queryset = models.Perdas.objects.all()