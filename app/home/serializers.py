from rest_framework import serializers
from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()
    
    class Meta:
        model = Aluno
        fields = '__all__'
        


    def get_history(self, obj):
        return [{'nome': h.nome, 'data': h.history_date, 'user': h.history_user, 'motivoAlteração': h.history_change_reason} for h in obj.history.all()]