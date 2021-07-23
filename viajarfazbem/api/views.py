# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .models import City, Country, Category, Routes, Item, Vitrine
from .serializers import CitySerializer, CountrySerializer, CategorySerializer, RoutersSerializer, \
    ItemSerializer, VitrineSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("hotel_name")
    serializer_class = ItemSerializer


class VitrineViewSet(viewsets.ModelViewSet):
    queryset = Vitrine.objects.all().order_by("title")
    serializer_class = VitrineSerializer

    def list(self, request, *args, **kwargs):
        print(request.data);
        headers = self.get_success_headers(request.data)
        vitrineSerializada = VitrineSerializer(Vitrine.objects.all(), many=True)
        return Response(vitrineSerializada.data, status=status.HTTP_201_CREATED, headers=headers)



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






