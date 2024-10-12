from django.contrib import admin
from .models import Cotegory, Product, Cart, Cartitem
# Register your models here.
admin.site.register(Cotegory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitem)
