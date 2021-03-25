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


def test_bulk_create_instance(inventorychange_set_factory, event_factory):
    inventorychange_set = inventorychange_set_factory()
    event = event_factory(
        event_type=ORDER_PRODUCT, inventorychange_set=inventorychange_set
    )
    InventoryChange.bulk_create_instance(
        event=event, inventorychange_set=inventorychange_set
    )

    assert inventorychange_set == list(
        event.inventorychange_set.values("product_id", "value")
    )
