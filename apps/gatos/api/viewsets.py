from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.gatos.models import Pessoas
from apps.gatos.api.serializes import PessoasSerializer
import requests

class PessoasViewSet(ModelViewSet):
    serializer_class = PessoasSerializer
    queryset = Pessoas.objects.all()
        