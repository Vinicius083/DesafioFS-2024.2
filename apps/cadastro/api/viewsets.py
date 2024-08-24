from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.cadastro.models import Cadastro
from apps.cadastro.api.serializers import CadastroSerializer
import requests

class CadastroViewSet(ModelViewSet):
    serializer_class = CadastroSerializer
    queryset = Cadastro.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)