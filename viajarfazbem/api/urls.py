from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'routes', views.RoutesViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'vitrine', views.VitrineViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
