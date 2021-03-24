from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

from core.models import TimestampedModel, Image


class ProductMaterial(TimestampedModel):
    """ 제품 재질 """

    name = models.CharField(_("이름"), max_length=50, unique=True)

    def __str__(self):
        return self.name


class ProductCategory(TimestampedModel):
    """ 제품 카테고리 """

    name = models.CharField(_("이름"), max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(TimestampedModel):
    """ 제품 """

    name = models.CharField(_("이름"), max_length=50, unique=True)
    barcode = models.CharField(_("바코드"), max_length=50, blank=True)
    description = models.TextField(_("설명"))
    materials = models.ManyToManyField("ProductMaterial", verbose_name=_("재질"))
    categories = models.ManyToManyField(
        "ProductCategory", verbose_name=_("카테고리")
    )
    price = models.PositiveIntegerField(_("가격"))
    price_with_pees = models.PositiveIntegerField(_("수수료포함 가격"))
    count = models.PositiveIntegerField(_("보유 수량"), default=0)
    archived = models.BooleanField(_("재입고 예정없음"), default=False)

    def __str__(self):
        return f"{self.name} : {self.count}"

    @classmethod
    def update_inventory(cls, store, product_id, value):
        obj = get_object_or_404(cls, pk=product_id)
        obj.count += value
        obj.save()
        return obj


class StoreProduct(TimestampedModel):
    """ 입점처 제품 """

    store = models.ForeignKey(
        "events.Store", verbose_name=_("입점처"), on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        "products.Product", verbose_name=_("제품"), on_delete=models.CASCADE,
    )
    count = models.IntegerField(_("재고 수량"))

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["store", "product"], name="store-product"
            )
        ]

    def __str__(self):
        return f"[{self.store.name}] {self.product.name} : {self.count}"

    @classmethod
    def update_inventory(cls, store, product_id, value):
        try:
            obj = cls.objects.get(store=store, product_id=product_id)
            obj.count += value
            obj.save()
        except cls.DoesNotExist:
            obj = cls.objects.create(
                store=store, product_id=product_id, count=value
            )
        return obj


class ProductImage(Image):
    """ 제품 사진 """

    product = models.ForeignKey(
        "Product",
        verbose_name=_("제품"),
        related_name="images",
        on_delete=models.CASCADE,
    )
