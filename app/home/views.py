from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

def index(request):
    alunos = Aluno.objects.all().values()
    template = loader.get_template('home/index.html')

    context = {
        'alunos': alunos
    }
    return HttpResponse(template.render(context, request))


# return render(request, 'home/index.html')

