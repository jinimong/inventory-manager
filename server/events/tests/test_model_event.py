from core.constants import SELL_DIRECT
import pytest


@pytest.fixture
def event(event_factory):
    return event_factory()


def test_str(event):
    assert str(event) == event.get_event_type_display()
