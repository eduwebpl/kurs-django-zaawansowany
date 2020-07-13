from core.functions import get_parsed_value_to_int_or_none


def test_get_parsed_value_to_int_or_none():
    result = get_parsed_value_to_int_or_none("1")
    assert result == 1
