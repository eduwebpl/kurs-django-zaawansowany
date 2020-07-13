import pytest
from django.utils.translation import override


@pytest.fixture(autouse=True)
def autouse_db(db):
    pass


def set_en_language():
    with override("en"):
        yield
