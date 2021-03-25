import pytest


@pytest.fixture
def material(product_material_factory):
    return product_material_factory()


def test_str(material):
    assert str(material) == material.name
