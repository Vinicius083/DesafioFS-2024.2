from rest_framework import serializers
from apps.cadastro.models import Cadastro

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = [
            'id',
            'nome',
            'sobrenome',
            'idade'
        ]