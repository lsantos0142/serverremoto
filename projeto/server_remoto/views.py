from django.shortcuts import render

# Create your views here.

def menu_inicial(request):
    return render(request, "menu_inicial.html", {})