from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from graphene_file_upload.django import FileUploadGraphQLView

from .schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "graphql/",
        csrf_exempt(
            FileUploadGraphQLView.as_view(
                graphiql=settings.DEBUG, schema=schema
            )
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
