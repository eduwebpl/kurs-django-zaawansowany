from unittest import TestCase

from core.functions import get_parsed_value_to_int_or_none


class TestIntParser(TestCase):
    def test_get_parsed_value_to_int_or_none(self):
        result = get_parsed_value_to_int_or_none("1")
        self.assertEqual(result, 1)
