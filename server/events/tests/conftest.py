import pytest

from typing import Callable
from events.models import EVENT_TYPE_CHOICES, Event, Store


@pytest.fixture
def store_factory(faker) -> Callable[[str], Store]:
    def factory(name=None, description=None):
        return Store.objects.create(
            name=name or faker.slug(),
            description=description or faker.sentence(),
        )

    return factory


@pytest.fixture
def inventorychange_set_factory(faker, product_factory):
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
def inventorychange_set_factory_from_store(faker):
    def factory(store: Store):
        products = {
            store_product.product_id: store_product.count
            for store_product in store.storeproduct_set.values_list(
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


@pytest.fixture
def event_factory(faker):
    def factory(
        event_type=None,
        store: Store = None,
        description=None,
        inventorychange_set=[],
    ):
        return Event.create_instance(
            inventorychange_set=inventorychange_set,
            event_type=event_type
            or faker.random_element(
                elements=[choice[0] for choice in EVENT_TYPE_CHOICES]
            ),
            store=store,
            description=description or faker.sentence(),
        )

    return factory
