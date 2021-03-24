import pytest


@pytest.fixture(scope="function")
def category(product_category_factory):
    return product_category_factory()


def test_str(category):
    assert str(category) == category.name
