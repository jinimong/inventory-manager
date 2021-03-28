from products.models import ProductCategory


def test_create(product_category_factory):
    assert 0 == ProductCategory.objects.count()

    category = product_category_factory()
    assert 1 == ProductCategory.objects.count()
    assert category.name == ProductCategory.objects.last().name
