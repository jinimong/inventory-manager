import pytest


@pytest.fixture(scope="function")
def store(store_factory):
    return store_factory()


def test_str(store):
    assert str(store) == store.name

