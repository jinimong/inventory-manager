from products.models import ProductMaterial


def test_create(product_material_factory):
    assert 0 == ProductMaterial.objects.count()

    material = product_material_factory()
    assert 1 == ProductMaterial.objects.count()
    assert material.name == ProductMaterial.objects.last().name
