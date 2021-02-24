from django.db import models
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
        return self.name


class ProductImage(Image):
    """ 제품 사진 """

    product = models.ForeignKey(
        "Product", verbose_name=_("제품 사진"), on_delete=models.CASCADE
    )
