import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Paciente
from django.core import serializers

# Create your views here.

def menu_inicial(request):
    return render(request, "menu_inicial.html", {})

