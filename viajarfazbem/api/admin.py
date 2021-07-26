from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Item)
admin.site.register(Vitrine)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Routes)
