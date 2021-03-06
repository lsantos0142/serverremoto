"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from server_remoto import views

from rest_framework import routers
from server_remoto.api import viewsets

route = routers.DefaultRouter()

route.register(r'Pacientes', viewsets.PacienteViewSet, basename = "Pacientes")
route.register(r'Imunizacoes', viewsets.ImunizacaoViewSet, basename = "Imunizações")
route.register(r'Lotes', viewsets.LoteViewSet, basename = "Lotes")
route.register(r'Perdas', viewsets.PerdasViewSet, basename = "Perdas")
route.register(r'Atualizar', viewsets.AtualizaServerViewSet, basename = "Atualizar")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('', views.menu_inicial, name = "menu")
]
