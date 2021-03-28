from products.models import Product


def test_create(product_factory):
    assert 0 == Product.objects.count()

    product = product_factory()
    assert 1 == Product.objects.count()
    assert product.name == Product.objects.last().name
