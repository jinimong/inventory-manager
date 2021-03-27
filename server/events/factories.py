import factory
from events.models import EVENT_TYPE_CHOICES


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "events.Store"
        django_get_or_create = ("name",)

    name = factory.Faker("slug")
    description = factory.Faker("sentence")
