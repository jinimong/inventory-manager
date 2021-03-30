from products.models import Product


def test_create(product_factory):
    assert 0 == Product.objects.count()

    product = product_factory()
    assert 1 == Product.objects.count()
    assert product.name == Product.objects.last().name


def test_create_with_materials(product_factory, product_material_factory):
    material_1 = product_material_factory()
    material_2 = product_material_factory()
    product = product_factory(materials=[material_1, material_2])
    assert set(product.materials.values_list("id", flat=True)) == set(
        [material_1.id, material_2.id]
    )


def test_create_with_categories(product_factory, product_category_factory):
    category_1 = product_category_factory()
    category_2 = product_category_factory()
    product = product_factory(categories=[category_1, category_2])
    assert set(product.categories.values_list("id", flat=True)) == set(
        [category_1.id, category_2.id]
    )
