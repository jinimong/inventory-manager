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
    all_stores = graphene.List(StoreType)
    all_events = graphene.List(EventType)

    def resolve_all_stores(self, info, **kwargs):
        return Store.objects.all()

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
    product_id = graphene.Int()
    value = graphene.Int()


class EventInput(graphene.InputObjectType):
    event_type = graphene.String()
    store_id = graphene.Int()
    inventorychange_set = graphene.List(InventoryChangeInput)
    description = graphene.String(required=False)


class CreateEvent(graphene.Mutation):
    event = graphene.Field(EventType)

    class Arguments:
        event_input = EventInput()

    @transaction.atomic
    def mutate(self, info, event_input):
        inventorychange_set = event_input.pop("inventorychange_set")
        event = Event.create_instance(inventorychange_set, **event_input)
        InventoryChange.bulk_create_instance(event, inventorychange_set)
        return CreateEvent(event=event)


class Mutation(graphene.ObjectType):
    create_store = CreateStore.Field()
    create_event = CreateEvent.Field()
