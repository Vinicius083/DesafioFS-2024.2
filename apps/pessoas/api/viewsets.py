from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.pessoas.models import Pessoas
from apps.pessoas.api.serializers import PessoaSerializer
import requests

class PessoasViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoas.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)