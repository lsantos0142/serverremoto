from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Paciente

# Create your views here.

def menu_inicial(request):
    return render(request, "menu_inicial.html", {})

def sincronizar(request):
    if request.method == "POST":
        x = request.POST
    return JsonResponse({x})