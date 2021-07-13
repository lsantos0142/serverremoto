from rest_framework import viewsets
from server_remoto import models
from server_remoto.api import serializers

class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PacienteSerializer
    queryset = models.Paciente.objects.all()

class ImunizacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImunizacaoSerializer
    queryset = models.Imunizacao.objects.all()

class LoteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LoteSerializer
    queryset = models.Lote.objects.all()

class PerdasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PerdasSerializer
    queryset = models.Perdas.objects.all()