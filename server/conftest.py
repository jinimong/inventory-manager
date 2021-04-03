import pytest
import shutil

from django.utils import timezone
from graphene.test import Client
from graphene_file_upload.django.testing import file_graphql_query
from pytest_factoryboy import register
from config.schema import schema
from products.models import ProductImage
from products.factories import ProductFactory

register(ProductFactory)


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="session", autouse=True)
def faker_session_locale():
    return ["ko_KR"]


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return timezone.now()


@pytest.fixture(scope="session")
def client():
    return Client(schema=schema)


@pytest.fixture
def use_test_media_root(settings):
    ProductImage.photo.field.upload_to = ""
    settings.MEDIA_ROOT += "/test"
    settings.MEDIA_URL = "/media/test/"

    yield

    shutil.rmtree(settings.MEDIA_ROOT)


@pytest.fixture(scope="session")
def file_upload_client():
    def func(*args, **kwargs):
        return file_graphql_query(*args, **kwargs)

    return func
