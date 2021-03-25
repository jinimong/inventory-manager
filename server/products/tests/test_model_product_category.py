import pytest


@pytest.fixture
def category(product_category_factory):
    return product_category_factory()


def test_str(category):
    assert str(category) == category.name
