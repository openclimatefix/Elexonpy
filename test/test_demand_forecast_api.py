# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.demand_forecast_api import DemandForecastApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDemandForecastApi(unittest.TestCase):
    """DemandForecastApi unit test stubs"""

    def setUp(self):
        self.api = DemandForecastApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_forecast_demand_daily_evolution_get(self):
        """Test case for forecast_demand_daily_evolution_get

        Evolution of the fourteen-day demand forecast over time (NDFD, TSDFD)  # noqa: E501
        """
        pass

    def test_forecast_demand_daily_get(self):
        """Test case for forecast_demand_daily_get

        Fourteen day demand forecast (NDFD, TSDFD)  # noqa: E501
        """
        pass

    def test_forecast_demand_daily_history_get(self):
        """Test case for forecast_demand_daily_history_get

        History of the fourteen-day demand forecast (NDFD, TSDFD)  # noqa: E501
        """
        pass

    def test_forecast_demand_day_ahead_earliest_get(self):
        """Test case for forecast_demand_day_ahead_earliest_get

        Historic view of the earliest forecasted demand (NDF, TSDF)  # noqa: E501
        """
        pass

    def test_forecast_demand_day_ahead_earliest_stream_get(self):
        """Test case for forecast_demand_day_ahead_earliest_stream_get

        Historic view of the earliest forecasted demand (NDF, TSDF) stream  # noqa: E501
        """
        pass

    def test_forecast_demand_day_ahead_evolution_get(self):
        """Test case for forecast_demand_day_ahead_evolution_get

        Evolution of the day-ahead demand forecast over time (NDF, TSDF)  # noqa: E501
        """
        pass

    def test_forecast_demand_day_ahead_get(self):
        """Test case for forecast_demand_day_ahead_get

        Day-ahead demand forecast (NDF, TSDF)  # noqa: E501
        """
        pass

    def test_forecast_demand_day_ahead_history_get(self):
        """Test case for forecast_demand_day_ahead_history_get

        History of the day-ahead demand forecast (NDF, TSDF)  # noqa: E501
        """
        pass

    def test_forecast_demand_day_ahead_latest_get(self):
        """Test case for forecast_demand_day_ahead_latest_get

        Historic view of the latest forecasted demand (NDF, TSDF)  # noqa: E501
        """
        pass

    def test_forecast_demand_day_ahead_latest_stream_get(self):
        """Test case for forecast_demand_day_ahead_latest_stream_get

        Historic view of the latest forecasted demand (NDF, TSDF) stream  # noqa: E501
        """
        pass

    def test_forecast_demand_day_ahead_peak_get(self):
        """Test case for forecast_demand_day_ahead_peak_get

        Peak forecasted demand per day (TSDF)  # noqa: E501
        """
        pass

    def test_forecast_demand_total_day_ahead_get(self):
        """Test case for forecast_demand_total_day_ahead_get

        Day-ahead total load forecast (DATL/B0620)  # noqa: E501
        """
        pass

    def test_forecast_demand_total_week_ahead_get(self):
        """Test case for forecast_demand_total_week_ahead_get

        Week-ahead total load forecast (WATL/B0630)  # noqa: E501
        """
        pass

    def test_forecast_demand_total_week_ahead_latest_get(self):
        """Test case for forecast_demand_total_week_ahead_latest_get

        Latest week-ahead total load forecast (WATL/B0630)  # noqa: E501
        """
        pass

    def test_forecast_demand_weekly_evolution_get(self):
        """Test case for forecast_demand_weekly_evolution_get

        Evolution of the one-year demand forecast over time  (NDFW, TSDFW)  # noqa: E501
        """
        pass

    def test_forecast_demand_weekly_get(self):
        """Test case for forecast_demand_weekly_get

        One-year demand forecast (NDFW, TSDFW)  # noqa: E501
        """
        pass

    def test_forecast_demand_weekly_history_get(self):
        """Test case for forecast_demand_weekly_history_get

        History of the one-year demand forecast (NDFW, TSDFW)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()