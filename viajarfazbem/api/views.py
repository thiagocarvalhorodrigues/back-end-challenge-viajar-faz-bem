# Create your views here.
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by("name")
    serializer_class = CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by("name")
    serializer_class = CountrySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Routes.objects.all().order_by("path")
    serializer_class = RoutersSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("hotel_name")
    serializer_class = ItemSerializer


class VitrineViewSet(viewsets.ModelViewSet):
    queryset = Vitrine.objects.all().order_by("title")
    serializer_class = VitrineSerializer

    ## Função criada com POST, passando como parâmentro o Payload recebdo um Json ##
    def create(self, request, *args, **kwargs):
        dados = request.data
        routes = (dados['routes'])
        queryset = VitrineSerializer(Vitrine.objects.filter(routes__path=routes), many=True)
        return Response(queryset.data, status=status.HTTP_200_OK)
