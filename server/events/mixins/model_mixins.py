from collections import namedtuple
from core.constants import (
    SELL_DIRECT,
    ORDER_PRODUCT,
    SEND_PRODUCT,
    SETTLE_SALE,
    LEAVE_STORE,
    DEFECT_PRODUCT_IN_STORE,
    DEFECT_PRODUCT_IN_HOME,
)
from products.models import Product, StoreProduct

EventProcess = namedtuple("EventProcess", ["model", "weight"])
EVENT_TYPE_PROCESS = {
    SELL_DIRECT: [EventProcess(Product, -1)],
    ORDER_PRODUCT: [EventProcess(Product, 1)],
    SEND_PRODUCT: [EventProcess(Product, -1), EventProcess(StoreProduct, 1)],
    SETTLE_SALE: [EventProcess(StoreProduct, -1)],
    LEAVE_STORE: [EventProcess(StoreProduct, -1), EventProcess(Product, 1)],
    DEFECT_PRODUCT_IN_STORE: [EventProcess(StoreProduct, -1)],
    DEFECT_PRODUCT_IN_HOME: [EventProcess(Product, -1)],
}


class EventMixin:
    @classmethod
    def create_instance(cls, inventory_changes, **input_kwargs):
        """ 이벤트 인스턴스 생성 """
        event = cls.objects.create(**input_kwargs)
        event._process_by_event_type(inventory_changes)
        return event

    def _process_by_event_type(self, inventory_changes) -> None:
        """ 이벤트타입에 따른 재고 처리 """
        processes = EVENT_TYPE_PROCESS[self.event_type]

        for process in processes:
            for inventorychange in inventory_changes:
                product_id = inventorychange.get("product_id")
                value = inventorychange.get("value", 0) * process.weight
                process.model.update_inventory(self.store, product_id, value)


class InventoryChangeMixin:
    @classmethod
    def bulk_create_instance(cls, event, inventory_changes):
        """ 이벤트 인스턴스 생성 """
        cls.objects.bulk_create(
            [
                cls(
                    event=event,
                    product_id=inventorychange.get("product_id"),
                    value=abs(inventorychange.get("value")),
                )
                for inventorychange in inventory_changes
            ]
        )
