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


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("hotel_name")
    serializer_class = ItemSerializer


class VitrineViewSet(viewsets.ModelViewSet):
    queryset = Vitrine.objects.all().order_by("title")
    serializer_class = VitrineSerializer

    """ Função criada com POST, recendo como parâmentro o Payload recebdio um json """
    def create(self, request, *args, **kwargs):
        dados = request.data
        routes_request = (dados['routes'])
        queryset = VitrineSerializer(Vitrine.objects.filter(routes__contains=routes_request), many=True)
        return Response(queryset.data, status=status.HTTP_200_OK)
