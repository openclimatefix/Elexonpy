# coding: utf-8

"""
    Insights API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import elexonpy
from elexonpy.api.generation_api import GenerationApi  # noqa: E501
from elexonpy.rest import ApiException


class TestGenerationApi(unittest.TestCase):
    """GenerationApi unit test stubs"""

    def setUp(self):
        self.api = GenerationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_generation_actual_per_type_day_total(self):
        """Test case for get_generation_actual_per_type_day_total

        Current snapshot of actual generation by fuel type categories (AGPT/B1620)  # noqa: E501
        """
        pass

    def test_get_generation_actual_per_type_from_from_to_to(self):
        """Test case for get_generation_actual_per_type_from_from_to_to

        Historic actual generation automatically down-sampled (AGPT/B1620)  # noqa: E501
        """
        pass

    def test_get_generation_actual_per_type_wind_and_solar_from_from_to_to(self):
        """Test case for get_generation_actual_per_type_wind_and_solar_from_from_to_to

        Historic actual or estimated wind and solar power generation (AGWS/B1630)  # noqa: E501
        """
        pass

    def test_get_generation_outturn(self):
        """Test case for get_generation_outturn

        Total generation outturn (FUELINST)  # noqa: E501
        """
        pass

    def test_get_generation_outturn_current(self):
        """Test case for get_generation_outturn_current

        Current snapshot of generation by fuel type categories (FUELINST, FUELHH)  # noqa: E501
        """
        pass

    def test_get_generation_outturn_fuelinsthhcur(self):
        """Test case for get_generation_outturn_fuelinsthhcur

        This endpoint is obsolete, and this location may be removed with no further notice.   # noqa: E501
        """
        pass

    def test_get_generation_outturn_halfhourlyinterconnector(self):
        """Test case for get_generation_outturn_halfhourlyinterconnector

        This endpoint is obsolete, and this location may be removed with no further notice.   # noqa: E501
        """
        pass

    def test_get_generation_outturn_interconnectors(self):
        """Test case for get_generation_outturn_interconnectors

        Historic half-hourly interconnector flows (FUELINST)  # noqa: E501
        """
        pass

    def test_get_generation_outturn_summary(self):
        """Test case for get_generation_outturn_summary

        Historic generation automatically down-sampled (FUELINST)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
