from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill

from core.utils import uuid_upload_to


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimestampedModel):
    photo = ProcessedImageField(
        upload_to=uuid_upload_to,
        blank=True,
        processors=[ResizeToFill(120, 120)],
        format="JPEG",
        options={"quality": 70},
    )
    photo_thumbnail = ImageSpecField(
        source="photo",
        processors=[Thumbnail(40, 40)],
        format="JPEG",
        options={"quality": 70},
    )

    class Meta:
        abstract = True
