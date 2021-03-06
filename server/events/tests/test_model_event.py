import pytest

from collections import Counter
from core.constants import (
    DEFECT_PRODUCT_IN_HOME,
    DEFECT_PRODUCT_IN_STORE,
    LEAVE_STORE,
    ORDER_PRODUCT,
    SELL_DIRECT,
    SEND_PRODUCT,
    SETTLE_SALE,
)
from events.models import Store
from products.models import Product


@pytest.fixture
def store(faker, store_factory, product_factory):
    store = store_factory()
    for _ in range(faker.random_digit_not_null()):
        product = product_factory()
        product.store_products.create(
            store=store, count=faker.random_int(min=1, max=100)
        )
    return store


def get_product_counter():
    return (
        Counter(
            {
                product.id: product.count
                for product in Product.objects.values_list(
                    "id", "count", named=True
                ).iterator()
            }
        )
        + Counter()
    )


def get_store_product_counter(store: Store):
    return (
        Counter(
            {
                store_product.product_id: store_product.count
                for store_product in store.store_products.values_list(
                    "product_id", "count", named=True
                ).iterator()
            }
        )
        + Counter()
    )


def get_diff(inventory_changes):
    return Counter(
        {change["product_id"]: change["value"] for change in inventory_changes}
    )


def test_str(event_factory):
    event = event_factory()
    assert str(event) == event.get_event_type_display()


def test_process_sell_direct(event_factory, inventory_changes_factory):
    """
    개인판매
      - Product 의 count 가 재고변화만큼 줄어든다
    """
    event = event_factory(event_type=SELL_DIRECT)
    inventory_changes = inventory_changes_factory()
    prev_products = get_product_counter()
    event._process_by_event_type(inventory_changes)
    diff = get_diff(inventory_changes)
    current_products = get_product_counter()
    assert prev_products - diff == current_products


def test_process_order_product(event_factory, inventory_changes_factory):
    """
    제품발주
      - Product 의 count 가 재고변화만큼 늘어난다
    """
    event = event_factory(event_type=ORDER_PRODUCT)
    inventory_changes = inventory_changes_factory()
    prev_products = get_product_counter()
    event._process_by_event_type(inventory_changes)
    diff = get_diff(inventory_changes)
    current_products = get_product_counter()
    assert prev_products + diff == current_products


def test_process_send_product(
    event_factory, store, inventory_changes_factory,
):
    """
    입점처 입고
      - Product 의 count 가 재고변화만큼 줄어든다
      - StoreProduct 의 count 가 재고변화만큼 늘어난다
    """
    event = event_factory(event_type=SEND_PRODUCT, store=store)
    inventory_changes = inventory_changes_factory()
    prev_products = get_product_counter()
    prev_store_products = get_store_product_counter(store)
    event._process_by_event_type(inventory_changes)
    diff = get_diff(inventory_changes)
    current_products = get_product_counter()
    current_store_products = get_store_product_counter(store)
    assert prev_products - diff == current_products
    assert prev_store_products + diff == current_store_products


def test_process_settle_sale(
    event_factory, store, inventory_changes_factory_from_store,
):
    """
    판매내역정산
      - StoreProduct 의 count 가 재고변화만큼 줄어든다
    """
    event = event_factory(event_type=SETTLE_SALE, store=store)
    inventory_changes = inventory_changes_factory_from_store(store)
    prev_store_products = get_store_product_counter(store)
    event._process_by_event_type(inventory_changes)
    diff = get_diff(inventory_changes)
    current_store_products = get_store_product_counter(store)
    assert prev_store_products - diff == current_store_products


def test_process_leave_store(
    event_factory, store, inventory_changes_factory_from_store,
):
    """
    입점처 퇴점
      - StoreProduct 의 count 가 재고변화만큼 줄어든다
      - Product 의 count 가 재고변화만큼 늘어난다
    """
    event = event_factory(event_type=LEAVE_STORE, store=store)
    inventory_changes = inventory_changes_factory_from_store(store)
    prev_products = get_product_counter()
    prev_store_products = get_store_product_counter(store)
    event._process_by_event_type(inventory_changes)
    diff = get_diff(inventory_changes)
    current_products = get_product_counter()
    current_store_products = get_store_product_counter(store)
    assert prev_store_products - diff == current_store_products
    assert prev_products + diff == current_products


def test_process_defect_product_in_store(
    event_factory, store, inventory_changes_factory_from_store
):
    """
    불량:입점처
      - StoreProduct 의 count 가 재고변화만큼 줄어든다
    """
    event = event_factory(event_type=DEFECT_PRODUCT_IN_STORE, store=store)
    inventory_changes = inventory_changes_factory_from_store(store)
    prev_store_products = get_store_product_counter(store)
    event._process_by_event_type(inventory_changes)
    diff = get_diff(inventory_changes)
    current_store_products = get_store_product_counter(store)
    assert prev_store_products - diff == current_store_products


def test_process_defect_product_in_home(
    event_factory, inventory_changes_factory
):
    """
    불량:집
      - Product 의 count 가 재고변화만큼 줄어든다
    """
    event = event_factory(event_type=DEFECT_PRODUCT_IN_HOME)
    inventory_changes = inventory_changes_factory()
    prev_products = get_product_counter()
    event._process_by_event_type(inventory_changes)
    diff = get_diff(inventory_changes)
    current_products = get_product_counter()
    assert prev_products - diff == current_products
