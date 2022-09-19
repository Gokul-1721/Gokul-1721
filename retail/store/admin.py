from django.contrib import admin
from .models import Product,Category

myModels=[Product,Category]
admin.site.register(myModels)


# Register your models here.
