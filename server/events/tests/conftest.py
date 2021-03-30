import pytest

from pytest_factoryboy import register
from events.factories import EventFactory, InventoryChangeFactory, StoreFactory
from events.models import Store

register(StoreFactory)
register(EventFactory)
register(InventoryChangeFactory)


@pytest.fixture
def inventory_changes_factory(faker, product_factory):
    def factory():
        result = []
        for _ in range(faker.random_digit_not_null()):
            product = product_factory()
            result.append(
                {
                    "product_id": product.id,
                    "value": faker.random_int(min=1, max=product.count),
                }
            )
        return result

    return factory


@pytest.fixture
def inventory_changes_factory_from_store(faker):
    def factory(store: Store):
        products = {
            store_product.product_id: store_product.count
            for store_product in store.store_products.values_list(
                "product_id", "count", named=True
            )
        }
        return [
            {
                "product_id": choice,
                "value": faker.random_int(min=1, max=products.get(choice, 1)),
            }
            for choice in set(faker.random_choices(elements=products.keys()))
        ]

    return factory
