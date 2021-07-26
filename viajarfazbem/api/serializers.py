from rest_framework import serializers
from .models import City, Item, Country, Category, Routes, Vitrine


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "name", "slug", "state"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "name", "slug"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "name", "slug"


class RoutersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        # fields = "path",
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True, many=True)
    country = CountrySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = "hotel_name", "slug", "image", "city", "country", "category", "price"


class VitrineSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True, many=True)
    routes = RoutersSerializer(read_only=True, many=True)

    class Meta:
        model = Vitrine
        # fields = "title", "subtitle", "routes", "item"
        fields = "__all__"
