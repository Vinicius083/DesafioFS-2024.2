from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.piadas.api.viewsets import PiadaViewSet

router = DefaultRouter()
router.register(r'piadas', PiadaViewSet, basename='piada')

urlpatterns = [
    path('', include(router.urls)),
]
