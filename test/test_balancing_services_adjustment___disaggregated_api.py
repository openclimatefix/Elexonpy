# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""



import unittest

import elexonpy
from elexonpy.api.balancing_services_adjustment___disaggregated_api import BalancingServicesAdjustmentDisaggregatedApi  # noqa: E501
from elexonpy.rest import ApiException


class TestBalancingServicesAdjustmentDisaggregatedApi(unittest.TestCase):
    """BalancingServicesAdjustmentDisaggregatedApi unit test stubs"""

    def setUp(self):
        self.api = BalancingServicesAdjustmentDisaggregatedApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_balancing_nonbm_disbsad_details_get(self):
        """Test case for balancing_nonbm_disbsad_details_get

        Disaggregated balancing services adjustment per settlement period (DISBSAD)  # noqa: E501
        """
        pass

    def test_balancing_nonbm_disbsad_summary_get(self):
        """Test case for balancing_nonbm_disbsad_summary_get

        Disaggregated balancing services adjustment time series (DISBSAD)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
