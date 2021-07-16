from rest_framework import viewsets
from server_remoto import models
from server_remoto.api import serializers
from rest_framework.response import Response

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

class LoteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LoteSerializer
    queryset = models.Lote.objects.all()

class PerdasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PerdasSerializer
    queryset = models.Perdas.objects.all()