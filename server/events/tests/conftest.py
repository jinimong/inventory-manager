import pytest

from typing import Callable
from events.models import EVENT_TYPE_CHOICES, Event, Store


@pytest.fixture
def store_factory(faker) -> Callable[[str], Store]:
    def factory(name=faker.slug(), description=faker.sentence()):
        return Store.objects.create(name=name, description=description)

    return factory


@pytest.fixture
def event_factory(faker):
    def factory(
        event_type=faker.random_element(
            elements=[choice[0] for choice in EVENT_TYPE_CHOICES]
        ),
        store: Store = None,
        description=faker.sentence(),
        inventorychange_set=[],
    ):
        return Event.create_instance(
            inventorychange_set=inventorychange_set,
            event_type=event_type,
            store=store,
            description=description,
        )

    return factory
