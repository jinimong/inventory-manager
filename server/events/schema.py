import graphene

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
    all_inventory_changes = graphene.List(InventoryChangeType)

    def resolve_all_stores(self, info, **kwargs):
        return Store.objects.all()

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_all_inventory_changes(self, info, **kwargs):
        return InventoryChange.objects.all()

