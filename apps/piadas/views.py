from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class PiadaViewSet(APIView):
    def get(self, request):
        url = 'https://geek-jokes.sameerkumar.website/api?format=json'
        response = requests.get(url)
        if response.status_code == 200:
            piada = response.json
            return response(piada)
        return response({"erro": "Não foi possivel obter a piada :("}, status=response.status_code)