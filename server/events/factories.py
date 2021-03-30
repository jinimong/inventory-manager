import factory
from events.models import EVENT_TYPES_ABOUT_STORE, EVENT_TYPE_CHOICES


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "events.Store"
        django_get_or_create = ("name",)

    name = factory.Faker("slug")
    description = factory.Faker("sentence")


class InventoryChangeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "events.InventoryChange"

    event = None
    product = factory.SubFactory("products.factories.ProductFactory")
    value = factory.Faker("random_int", min=1, max=1000)


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "events.Event"

    class Params:
        has_store = factory.LazyAttribute(
            lambda o: o.event_type in EVENT_TYPES_ABOUT_STORE
        )

    event_type = factory.Faker(
        "random_element", elements=[choice[0] for choice in EVENT_TYPE_CHOICES]
    )
    description = factory.Sequence(lambda n: f"event_{n}")
    store = factory.Maybe(
        "has_store",
        yes_declaration=factory.SubFactory(StoreFactory),
        no_declaration=None,
    )
    inventory_changes = factory.RelatedFactoryList(
        InventoryChangeFactory, factory_related_name="event",
    )
