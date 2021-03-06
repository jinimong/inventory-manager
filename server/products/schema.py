import graphene

from django.db import transaction

from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload

from .models import (
    ProductMaterial,
    ProductCategory,
    Product,
    StoreProduct,
    ProductImage,
)


class ProductMaterialType(DjangoObjectType):
    class Meta:
        model = ProductMaterial


class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCategory


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class StoreProductType(DjangoObjectType):
    class Meta:
        model = StoreProduct


class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage

    photo_thumbnail = graphene.String()

    def resolve_photo(self, info, **kwargs):
        return getattr(self.photo, "url")

    def resolve_photo_thumbnail(self, info, **kwargs):
        return getattr(self.photo_thumbnail, "url")


class Query(graphene.ObjectType):
    material = graphene.Field(ProductMaterialType, id=graphene.Int())
    all_materials = graphene.List(ProductMaterialType)
    category = graphene.Field(ProductCategoryType, id=graphene.Int())
    all_categories = graphene.List(ProductCategoryType)
    product = graphene.Field(ProductType, id=graphene.Int())
    all_products = graphene.List(ProductType)
    store_product = graphene.Field(StoreProductType, id=graphene.Int())
    all_store_products = graphene.List(StoreProductType)

    def resolve_material(self, info, **kwargs):
        return ProductMaterial.objects.get(id=kwargs.get("id"))

    def resolve_all_materials(self, info, **kwargs):
        return ProductMaterial.objects.all()

    def resolve_category(self, info, **kwargs):
        return ProductCategory.objects.get(id=kwargs.get("id"))

    def resolve_all_categories(self, info, **kwargs):
        return ProductCategory.objects.all()

    def resolve_product(self, info, **kwargs):
        return Product.objects.get(id=kwargs.get("id"))

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_store_product(self, info, **kwargs):
        return StoreProduct.objects.get(id=kwargs.get("id"))

    def resolve_all_store_products(self, info, **kwargs):
        return StoreProduct.objects.all()


class CreateProductMaterial(graphene.Mutation):
    material = graphene.Field(ProductMaterialType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, **kwargs):
        material = ProductMaterial(**kwargs)
        material.save()
        return CreateProductMaterial(material=material)


class CreateProductCategory(graphene.Mutation):
    category = graphene.Field(ProductCategoryType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, **kwargs):
        category = ProductCategory(**kwargs)
        category.save()
        return CreateProductCategory(category=category)


class ProductInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    barcode = graphene.String()
    description = graphene.String()
    materials = graphene.List(graphene.Int)
    categories = graphene.List(graphene.Int)
    price = graphene.Int(required=True)
    price_with_pees = graphene.Int(required=True)
    images = graphene.List(Upload)


class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        product_input = ProductInput()

    @transaction.atomic
    def mutate(self, info, product_input):
        m2m_fields = {
            field.name: product_input.pop(field.name)
            for field in Product._meta.many_to_many
            if field.name in product_input
        }

        related_fields = {
            field.name: product_input.pop(field.name)
            for field in Product._meta.related_objects
            if field.name in product_input
        }

        product = Product(**product_input)
        product.save()

        for field, value in m2m_fields.items():
            getattr(product, field).add(*value)

        for field, value in related_fields.items():
            related_manager = getattr(product, field)
            if type(value) == list:
                for v in value:
                    related_manager.create(**v)
            else:
                related_manager.create(**value)

        return CreateProduct(product=product)


class Mutation(graphene.ObjectType):
    create_material = CreateProductMaterial.Field()
    create_category = CreateProductCategory.Field()
    create_product = CreateProduct.Field()
