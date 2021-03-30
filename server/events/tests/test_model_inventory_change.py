from core.constants import ORDER_PRODUCT
from events.models import InventoryChange


def test_str(faker, event_factory, product_factory):
    event = event_factory()
    product = product_factory()
    inventory_change = InventoryChange.objects.create(
        event=event, product=product, value=faker.random_int()
    )
    assert (
        str(inventory_change) == f"{product.name} : {inventory_change.value}"
    )


def test_bulk_create_instance(inventory_changes_factory, event_factory):
    inventory_changes = inventory_changes_factory()
    event = event_factory(
        event_type=ORDER_PRODUCT, inventory_changes=inventory_changes
    )
    InventoryChange.bulk_create_instance(
        event=event, inventory_changes=inventory_changes
    )

    assert inventory_changes == list(
        event.inventory_changes.values("product_id", "value")
    )
