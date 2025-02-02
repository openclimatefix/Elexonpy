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
from elexonpy.api.availability_api import AvailabilityApi  # noqa: E501
from elexonpy.rest import ApiException


class TestAvailabilityApi(unittest.TestCase):
    """AvailabilityApi unit test stubs"""

    def setUp(self):
        self.api = AvailabilityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_generation_availability_summary14d(self):
        """Test case for get_generation_availability_summary14d

        [DEPRECATED] Fourteen-day generation forecast  # noqa: E501
        """
        pass

    def test_get_generation_availability_summary3yw(self):
        """Test case for get_generation_availability_summary3yw

        [DEPRECATED] Three-year generation forecast  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
