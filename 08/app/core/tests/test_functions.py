from unittest import mock

import requests

from core.functions import get_my_ip


class MockedResponse:

    def __init__(self, json_data) -> None:
        self.json_data = json_data

    def json(self):
        return self.json_data


@mock.patch.object(requests, "get")
def test_get_ip(get):
    get.return_value = MockedResponse(json_data={"ip": "127.0.0.1", "geo-ip": "https://getjsonip.com/#plus",
                                                 "API Help": "https://getjsonip.com/#docs"})
    assert get_my_ip() == "127.0.0.1"
