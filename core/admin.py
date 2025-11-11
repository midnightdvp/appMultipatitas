from django.contrib import admin
from .models import Product, Category, Accounts, Adress, County, Region, Sale, Comments, Detail

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Accounts)
admin.site.register(Adress)
admin.site.register(County)
admin.site.register(Region)
admin.site.register(Sale)
admin.site.register(Comments)
admin.site.register(Detail)