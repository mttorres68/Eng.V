from django.contrib import admin
from .models import Aluno
# Register your models here.

admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('name', 'escola', 'matricula', 'data_publicacao', 'data_nascimento')

admin.site.register(Aluno)