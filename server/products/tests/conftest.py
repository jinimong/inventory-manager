from pytest_factoryboy import register
from products.factories import (
    ProductMaterialFactory,
    ProductCategoryFactory,
    ProductFactory,
)

register(ProductMaterialFactory)
register(ProductCategoryFactory)
register(ProductFactory)
