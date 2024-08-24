from rest_framework import serializers
from apps.gatos import models

class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoas
        fields = [
            'id',
            'nome',
            'idade'
        ]