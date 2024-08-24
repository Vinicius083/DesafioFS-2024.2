from rest_framework import serializers
from apps.piadas.models import Piada

class PiadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piada
        fields = [
            'id',
            "conteudo",
            'criado_em'

        ]