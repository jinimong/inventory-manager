import factory


class ProductMaterialFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("slug")

    class Meta:
        model = "products.ProductMaterial"


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("slug")

    class Meta:
        model = "products.ProductCategory"


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("slug")
    count = factory.Faker("random_int", min=1, max=1000)
    price = 2000
    price_with_pees = factory.LazyAttribute(lambda o: o.price + 500)

    class Meta:
        model = "products.Product"
