from core.constants import (
    DEFECT_PRODUCT_IN_HOME,
    DEFECT_PRODUCT_IN_STORE,
    LEAVE_STORE,
    ORDER_PRODUCT,
    SELL_DIRECT,
    SEND_PRODUCT,
    SETTLE_SALE,
)
import graphene

from django.db import transaction

from graphene_django.types import DjangoObjectType

from .models import Store, Event, InventoryChange


class StoreType(DjangoObjectType):
    class Meta:
        model = Store


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class InventoryChangeType(DjangoObjectType):
    class Meta:
        model = InventoryChange


class Query(graphene.ObjectType):
    store = graphene.Field(StoreType, id=graphene.Int())
    all_stores = graphene.List(StoreType)
    event = graphene.Field(EventType, id=graphene.Int())
    all_events = graphene.List(EventType)

    def resolve_store(self, info, **kwargs):
        return Store.objects.get(id=kwargs.get("id"))

    def resolve_all_stores(self, info, **kwargs):
        return Store.objects.all()

    def resolve_event(self, info, **kwargs):
        return Event.objects.get(id=kwargs.get("id"))

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()


class CreateStore(graphene.Mutation):
    store = graphene.Field(StoreType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, **kwargs):
        store = Store(**kwargs)
        store.save()
        return CreateStore(store=store)


class InventoryChangeInput(graphene.InputObjectType):
    product_id = graphene.Int(required=True)
    value = graphene.Int(required=True)


class EventInput(graphene.InputObjectType):
    event_type = graphene.String(required=True)
    store_id = graphene.Int()
    inventory_changes = graphene.List(InventoryChangeInput)
    description = graphene.String()


class CreateEvent(graphene.Mutation):
    event = graphene.Field(EventType)

    class Arguments:
        event_input = EventInput()

    @transaction.atomic
    def mutate(self, info, event_input):
        inventory_changes = event_input.pop("inventory_changes")
        event = Event.create_instance(inventory_changes, **event_input)
        InventoryChange.bulk_create_instance(event, inventory_changes)
        return CreateEvent(event=event)


class BaseEventInput(graphene.InputObjectType):
    description = graphene.String()

    class Meta:
        abstract = True


class InventoryChangeFieldMixin(graphene.InputObjectType):
    inventory_changes = graphene.List(InventoryChangeInput)


class StoreFieldMixin(graphene.InputObjectType):
    store_id = graphene.Int()


class SellDirectInput(InventoryChangeFieldMixin, BaseEventInput):
    pass


class OrderProductInput(InventoryChangeFieldMixin, BaseEventInput):
    pass


class SendProductInput(
    InventoryChangeFieldMixin, StoreFieldMixin, BaseEventInput
):
    pass


class SettleSaleInput(
    InventoryChangeFieldMixin, StoreFieldMixin, BaseEventInput
):
    pass


class LeaveStoreInput(StoreFieldMixin, BaseEventInput):
    pass


class DefectProductInStoreInput(
    InventoryChangeFieldMixin, StoreFieldMixin, BaseEventInput
):
    pass


class DefectProductInHomeInput(InventoryChangeFieldMixin, BaseEventInput):
    pass


class BaseEventMutation(graphene.Mutation):
    event = graphene.Field(EventType)
    event_type = None

    class Meta:
        abstract = True

    class Arguments:
        input = None

    @classmethod
    @transaction.atomic
    def mutate(cls, root, info, input):
        inventory_changes = input.pop("inventory_changes", None)
        event = Event.create_instance(
            event_type=cls.event_type,
            inventory_changes=inventory_changes,
            **input
        )
        InventoryChange.bulk_create_instance(event, inventory_changes)
        return cls(event=event)


class SellDirect(BaseEventMutation):
    event_type = SELL_DIRECT

    class Arguments:
        input = SellDirectInput()


class OrderProduct(BaseEventMutation):
    event_type = ORDER_PRODUCT

    class Arguments:
        input = OrderProductInput()


class SendProduct(BaseEventMutation):
    event_type = SEND_PRODUCT

    class Arguments:
        input = SendProductInput()


class SettleSale(BaseEventMutation):
    event_type = SETTLE_SALE

    class Arguments:
        input = SettleSaleInput()


class LeaveStore(BaseEventMutation):
    event_type = LEAVE_STORE

    class Arguments:
        input = LeaveStoreInput()


class DefectProductInStore(BaseEventMutation):
    event_type = DEFECT_PRODUCT_IN_STORE

    class Arguments:
        input = DefectProductInStoreInput()


class DefectProductInHome(BaseEventMutation):
    event_type = DEFECT_PRODUCT_IN_HOME

    class Arguments:
        input = DefectProductInHomeInput()


class Mutation(graphene.ObjectType):
    create_store = CreateStore.Field()
    create_event = CreateEvent.Field()
    sell_direct = SellDirect.Field()
    order_product = OrderProduct.Field()
    send_product = SendProduct.Field()
    settle_sale = SettleSale.Field()
    leave_store = LeaveStore.Field()
    defect_product_in_store = DefectProductInStore.Field()
    defect_product_in_home = DefectProductInHome.Field()
