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


class Mutation(graphene.ObjectType):
    create_store = CreateStore.Field()
    create_event = CreateEvent.Field()
