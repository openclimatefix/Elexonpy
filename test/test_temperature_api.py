# coding: utf-8

"""
    Insights API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.temperature_api import TemperatureApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTemperatureApi(unittest.TestCase):
    """TemperatureApi unit test stubs"""

    def setUp(self):
        self.api = TemperatureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_temperature(self):
        """Test case for get_temperature

        Temperature data (TEMP)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
