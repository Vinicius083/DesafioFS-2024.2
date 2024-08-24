from rest_framework import serializers
from apps.pessoas.models import Pessoas

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = [
            'id',
            'nome',
            'sobrenome',
            'idade'
        ]