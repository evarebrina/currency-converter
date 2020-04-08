import unittest
from unittest.mock import patch

from routers import convert


class TestConverter(unittest.TestCase):
    @patch("routers.get_usd_currency")
    def test_convert(self, get_usd_currency):
        get_usd_currency.return_value = 100
        assert {
            "currency": 100,
            "requested_value": 15,
            "resulting_value": 1500,
        } == convert({"value": 15})


if __name__ == "__main__":
    unittest.main()
