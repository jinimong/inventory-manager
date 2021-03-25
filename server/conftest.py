import pytest

from django.utils import timezone

# flake8: noqa: F401
from products.tests.conftest import product_factory


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="session", autouse=True)
def faker_session_locale():
    return ["ko_KR"]


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return timezone.now()
