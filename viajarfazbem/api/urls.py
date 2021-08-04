from django.urls import include, path
from rest_framework import routers
from .views import *

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'country', CountryViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'item', ItemViewSet)
router.register(r'vitrine', VitrineViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('openapi/', get_schema_view(
        title="API pacote de viagens",
        description="API para realizar a consulta de pacotes de viagens.",
        version="2.0"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

]
