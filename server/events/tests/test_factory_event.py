import pytest

from events.models import EVENT_TYPES_ABOUT_STORE, EVENT_TYPE_CHOICES, Event


def test_create(event_factory):
    assert 0 == Event.objects.count()

    event = event_factory()
    assert 1 == Event.objects.count()
    assert event.description == Event.objects.last().description


@pytest.mark.parametrize(
    "event_type", [choice[0] for choice in EVENT_TYPE_CHOICES]
)
def test_create_with_store(event_type, event_factory):
    event = event_factory(event_type=event_type)

    if event_type in EVENT_TYPES_ABOUT_STORE:
        assert event.store is not None
    else:
        assert event.store is None


@pytest.mark.parametrize("event_type", EVENT_TYPES_ABOUT_STORE)
def test_create_with_exist_store(event_type, store_factory, event_factory):
    store = store_factory()
    event = event_factory(event_type=event_type, store__name=store.name)
    assert event.store == store


def test_create_with_inventory_change(event_factory):
    event = event_factory()
    assert event.inventorychange_set.exists()
