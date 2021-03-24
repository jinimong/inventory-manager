import pytest

from typing import Callable
from products.models import ProductMaterial, ProductCategory, Product


@pytest.fixture
def product_material_factory(faker) -> Callable[[str], ProductMaterial]:
    def factory(name=faker.slug()):
        return ProductMaterial.objects.create(name=name)

    return factory


@pytest.fixture
def product_category_factory(faker) -> Callable[[str], ProductCategory]:
    def factory(name=faker.slug()):
        return ProductCategory.objects.create(name=name)

    return factory


@pytest.fixture
def product_factory(faker) -> Callable[[str], Product]:
    def factory(name=faker.slug(), count=faker.random_number()):
        return Product.objects.create(
            name=name, count=count, price=2000, price_with_pees=2500
        )

    return factory
