import pytest

from core.functions import get_parsed_value_to_int_or_none


@pytest.mark.parametrize(['value', 'value_expected'], (
        ("1", 1),
        ("-1", -1),
        ("0", 0),
        ("10000000000", 10000000000),
        ("-10000000000", -10000000000),
))
def test_get_parsed_value_to_int_or_none(value, value_expected):
    assert get_parsed_value_to_int_or_none(value) == value_expected


@pytest.fixture(params=["USD", "PLN", "EUR"])
def currency(request):
    return request.param


def test_currency(currency):
    print(currency)
