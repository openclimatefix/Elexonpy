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
from elexonpy.api.non_bm_stor_api import NonBMSTORApi  # noqa: E501
from elexonpy.rest import ApiException


class TestNonBMSTORApi(unittest.TestCase):
    """NonBMSTORApi unit test stubs"""

    def setUp(self):
        self.api = NonBMSTORApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_balancing_nonbm_stor_events_count_count(self):
        """Test case for get_balancing_nonbm_stor_events_count_count

        Non-BM STOR events (NONBM)  # noqa: E501
        """
        pass

    def test_get_balancing_nonbm_stor_from_from_to_to(self):
        """Test case for get_balancing_nonbm_stor_from_from_to_to

        Non-BM STOR time series (NONBM)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
