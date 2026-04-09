from django.contrib import admin
from .models import Logo
from .models import Brand, Product

admin.site.register(Logo)

admin.site.register(Brand)
admin.site.register(Product)