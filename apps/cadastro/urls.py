from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.cadastro.api.viewsets import CadastroViewSet

router = DefaultRouter()
router.register(r'cadastros', CadastroViewSet, basename='cadastro')

urlpatterns = [
    path('', include(router.urls)),
]
