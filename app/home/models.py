from django.db import models
from simple_history.models import HistoricalRecords

class Aluno(models.Model):
    nome = models.CharField(max_length=20, default='')
    escola = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    data_publicacao = models.CharField(max_length=50)
    data_nascimento = models.CharField(max_length=50)

    history = HistoricalRecords(excluded_fields=['escola', 'matricula', 'data_publicacao', 'data_nascimento'])

