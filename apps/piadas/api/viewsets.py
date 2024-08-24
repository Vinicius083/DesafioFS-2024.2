from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.piadas.models import Piada
from apps.piadas.api.serializers import PiadaSerializer
import requests

class PiadaViewSet(ModelViewSet):
    serializer_class = PiadaSerializer
    queryset = Piada.objects.all()

    @action(detail=False, methods=['get'])
    def procurar_piada(self, request):
        url = "https://geek-jokes.sameerkumar.website/api?format=json"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dado_piada = resposta.json()
            conteudo_piada = dado_piada.get('joke')
                
            piada = Piada.objects.create(conteudo=conteudo_piada)

            serializer = self.get_serializer(piada)
            return Response(serializer.data)
        return Response({"erro": "Não foi possivel encontrar a piada :("}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)