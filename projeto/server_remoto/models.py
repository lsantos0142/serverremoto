from django.db import models


# Create your models here.

class Paciente(models.Model):
    paciente = models.JSONField()