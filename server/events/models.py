from django.db import models
from django.utils.translation import gettext as _

from core.models import TimestampedModel, Image


SELL_DIRECT = "SD"
ORDER_PRODUCT = "OP"
SEND_PRODUCT = "SP"
SETTLE_SALE = "SS"
LEAVE_STORE = "LS"
DEFECT_PRODUCT_IN_STORE = "DS"
DEFECT_PRODUCT_IN_HOME = "DH"

EVENT_TYPE_CHOICES = (
    (SELL_DIRECT, "개인판매"),
    (ORDER_PRODUCT, "제품발주"),
    (SEND_PRODUCT, "입점처 입고"),
    (SETTLE_SALE, "판매내역정산"),
    (LEAVE_STORE, "입점처 퇴점"),
    (DEFECT_PRODUCT_IN_STORE, "불량:입점처"),
    (DEFECT_PRODUCT_IN_HOME, "불량:집"),
)


class Store(TimestampedModel):
    """ 입점처 """

    name = models.CharField(_("이름"), max_length=50, unique=True)
    description = models.TextField(_("설명"))

    def __str__(self):
        return self.name


class Event(TimestampedModel):
    """ 재고 변화 내역 """

    event_type = models.CharField(
        _("재고 변화 타입"), choices=EVENT_TYPE_CHOICES, max_length=2
    )
    store = models.ForeignKey(
        "Store",
        verbose_name=_("입점처"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    description = models.TextField(_("설명"))

    def __str__(self):
        return f"{self.get_event_type_display()} ({self.description})"


class InventoryChange(TimestampedModel):
    """ 재고 변화 """

    event = models.ForeignKey(
        "Event", verbose_name=_("재고 변화 내역"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product", verbose_name=_("제품"), on_delete=models.CASCADE
    )
    count = models.IntegerField(_("변화 수량"))

    def __str__(self):
        count = f"+{self.count}" if self.count > 0 else self.count
        return f"{self.product_id} {count}"
