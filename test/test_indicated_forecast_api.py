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
from swagger_client.api.indicated_forecast_api import IndicatedForecastApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIndicatedForecastApi(unittest.TestCase):
    """IndicatedForecastApi unit test stubs"""

    def setUp(self):
        self.api = IndicatedForecastApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_forecast_indicated_day_ahead(self):
        """Test case for get_forecast_indicated_day_ahead

        Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)  # noqa: E501
        """
        pass

    def test_get_forecast_indicated_day_ahead_evolution_settlementdate_settlementdate_set(self):
        """Test case for get_forecast_indicated_day_ahead_evolution_settlementdate_settlementdate_set

        Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)  # noqa: E501
        """
        pass

    def test_get_forecast_indicated_day_ahead_history_publishtime_publishtime(self):
        """Test case for get_forecast_indicated_day_ahead_history_publishtime_publishtime

        Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
