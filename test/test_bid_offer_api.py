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
from swagger_client.api.bid_offer_api import BidOfferApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBidOfferApi(unittest.TestCase):
    """BidOfferApi unit test stubs"""

    def setUp(self):
        self.api = BidOfferApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_balancing_bid_offer_all_get(self):
        """Test case for balancing_bid_offer_all_get

        Market-wide bid-offer data (BOD)  # noqa: E501
        """
        pass

    def test_balancing_bid_offer_get(self):
        """Test case for balancing_bid_offer_get

        Bid-offer data per BMU (BOD)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()