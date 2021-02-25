from django.contrib import admin

from .models import (
    ProductMaterial,
    ProductCategory,
    Product,
    StoreProduct,
    ProductImage,
)

admin.site.register(ProductMaterial)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(StoreProduct)
admin.site.register(ProductImage)
