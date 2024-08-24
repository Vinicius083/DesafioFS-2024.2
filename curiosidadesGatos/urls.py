from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.gatos.api.viewsets import PessoasViewSet

router = routers.DefaultRouter()
router.register(r'pessoas', PessoasViewSet, basename='pessoas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
