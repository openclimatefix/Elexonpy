# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""



import unittest

import elexonpy
from elexonpy.api.temperature_api import TemperatureApi  # noqa: E501
from elexonpy.rest import ApiException


class TestTemperatureApi(unittest.TestCase):
    """TemperatureApi unit test stubs"""

    def setUp(self):
        self.api = TemperatureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_temperature_get(self):
        """Test case for temperature_get

        Temperature data (TEMP)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
