import pytest

from typing import Callable
from products.models import ProductMaterial, ProductCategory, Product


@pytest.fixture
def product_material_factory(faker) -> Callable[[str], ProductMaterial]:
    def factory(name=None):
        return ProductMaterial.objects.create(name=name or faker.slug())

    return factory


@pytest.fixture
def product_category_factory(faker) -> Callable[[str], ProductCategory]:
    def factory(name=None):
        return ProductCategory.objects.create(name=name or faker.slug())

    return factory


@pytest.fixture
def product_factory(faker) -> Callable[[str], Product]:
    def factory(name=None, count=None):
        return Product.objects.create(
            name=name or faker.slug(),
            count=count or faker.random_int(min=1, max=1000),
            price=2000,
            price_with_pees=2500,
        )

    return factory
