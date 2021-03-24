import pytest

from django.utils import timezone


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="session", autouse=True)
def faker_session_locale():
    return ["ko_KR"]


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return timezone.now()
