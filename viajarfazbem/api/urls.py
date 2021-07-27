from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'country', CountryViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'item', ItemViewSet)
router.register(r'vitrine', VitrineViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

]
