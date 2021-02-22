import graphene

from graphene_django.types import DjangoObjectType

from .models import ProductMaterial, ProductCategory, Product, ProductImage


class ProductMaterialType(DjangoObjectType):
    class Meta:
        model = ProductMaterial


class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCategory


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage


class Query(graphene.ObjectType):
    all_materials = graphene.List(ProductMaterialType)
    all_categories = graphene.List(ProductCategoryType)
    all_products = graphene.List(ProductType)

    def resolve_all_materials(self, info, **kwargs):
        return ProductMaterial.objects.all()

    def resolve_all_categories(self, info, **kwargs):
        return ProductCategory.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()
