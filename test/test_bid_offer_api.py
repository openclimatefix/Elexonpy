# coding: utf-8

"""
    Insights API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""



import unittest

import elexonpy
from elexonpy.api.bid_offer_api import BidOfferApi  # noqa: E501
from elexonpy.rest import ApiException


class TestBidOfferApi(unittest.TestCase):
    """BidOfferApi unit test stubs"""

    def setUp(self):
        self.api = BidOfferApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s(self):
        """Test case for get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s

        Market-wide bid-offer data (BOD)  # noqa: E501
        """
        pass

    def test_get_balancing_bid_offer_bmunit_bmunit_from_from_to_to(self):
        """Test case for get_balancing_bid_offer_bmunit_bmunit_from_from_to_to

        Bid-offer data per BMU (BOD)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
