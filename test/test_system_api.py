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
from elexonpy.api.system_api import SystemApi  # noqa: E501
from elexonpy.rest import ApiException


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self):
        self.api = SystemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_system_demand_control_instructions(self):
        """Test case for get_system_demand_control_instructions

        Demand control instructions (DCI)  # noqa: E501
        """
        pass

    def test_get_system_frequency(self):
        """Test case for get_system_frequency

        System frequency (FREQ)  # noqa: E501
        """
        pass

    def test_get_system_frequency_stream(self):
        """Test case for get_system_frequency_stream

        System frequency (FREQ) stream  # noqa: E501
        """
        pass

    def test_get_system_warnings(self):
        """Test case for get_system_warnings

        System warnings (SYSWARN)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
