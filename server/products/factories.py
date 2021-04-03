import factory


class ProductMaterialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.ProductMaterial"

    name = factory.Faker("slug")


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.ProductCategory"

    name = factory.Faker("slug")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Product"
        django_get_or_create = ("name",)

    name = factory.Faker("slug")
    count = factory.Faker("random_int", min=1, max=1000)
    price = 2000
    price_with_pees = factory.LazyAttribute(lambda o: o.price + 500)

    @factory.post_generation
    def materials(self, create, extracted):
        if not create:
            return

        if extracted:
            self.materials.add(*extracted)

    @factory.post_generation
    def categories(self, create, extracted):
        if not create:
            return

        if extracted:
            self.categories.add(*extracted)
