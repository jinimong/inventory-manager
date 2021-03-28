from events.models import Store


def test_create(store_factory):
    assert 0 == Store.objects.count()

    store = store_factory()
    assert 1 == Store.objects.count()
    assert store.name == Store.objects.last().name
