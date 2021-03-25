import pytest


@pytest.fixture
def product(product_factory):
    return product_factory()


def test_str(product):
    assert str(product) == f"{product.name} : {product.count}"


def test_update_inventory(faker, product):
    count = product.count
    updated_count = faker.random_int(min=abs(count) * -1, max=abs(count))
    product._meta.model.update_inventory(
        store=None, product_id=product.id, value=updated_count
    )
    product.refresh_from_db()
    assert product.count == count + updated_count
