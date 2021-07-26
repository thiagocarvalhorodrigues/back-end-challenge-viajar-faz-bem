from django.db import models

# Create your models here.



class Country(models.Model):
    objects = None
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Category(models.Model):
        objects = None
        name = models.CharField(max_length=100)
        slug = models.CharField(max_length=100)

        def __str__(self):
            return self.name


class Routes(models.Model):
    objects = None
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.path

class City(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Item(models.Model):
    objects = None
    hotel_name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.01, blank=False)
    city = models.ManyToManyField(City, related_name="city")
    category = models.ManyToManyField(Category, related_name='category')
    country = models.ManyToManyField(Country,related_name='country')

    def __str__(self):
        return self.hotel_name

class Vitrine(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    routes = models.ManyToManyField(Routes, related_name='routes')
    item = models.ManyToManyField(Item, related_name='item')

    def __str__(self):
        return self.title
