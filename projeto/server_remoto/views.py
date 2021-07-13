import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Paciente
from django.core import serializers

# Create your views here.

def menu_inicial(request):
    return render(request, "menu_inicial.html", {})

def sincronizar(request):
    if request.method == "POST":
        x = {'foo': 'bar'}
        req_paciente = Paciente(paciente=x)
        req_paciente.save()
    numero_de_pacientes = Paciente.objects.all().count()
    for i in range(0,numero_de_pacientes):
        paci = Paciente.objects.all()[i]
        serialized_obj = serializers.serialize('json', [paci])
    return JsonResponse({Paciente.objects.all()})