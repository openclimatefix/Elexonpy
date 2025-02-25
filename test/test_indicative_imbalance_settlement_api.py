# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""



import unittest

import elexonpy
from elexonpy.api.indicative_imbalance_settlement_api import IndicativeImbalanceSettlementApi  # noqa: E501
from elexonpy.rest import ApiException


class TestIndicativeImbalanceSettlementApi(unittest.TestCase):
    """IndicativeImbalanceSettlementApi unit test stubs"""

    def setUp(self):
        self.api = IndicativeImbalanceSettlementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_get(self):
        """Test case for balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_get

        Acceptance volumes by settlement date (BOAV)  # noqa: E501
        """
        pass

    def test_balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_settlement_period_get

        Acceptance volumes by settlement period (BOAV)  # noqa: E501
        """
        pass

    def test_balancing_settlement_acceptances_all_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_acceptances_all_settlement_date_settlement_period_get

        Historic acceptances by settlement period (ISPSTACK, BOALF, BOD)  # noqa: E501
        """
        pass

    def test_balancing_settlement_default_notices_get(self):
        """Test case for balancing_settlement_default_notices_get

        Default notices (CDN)  # noqa: E501
        """
        pass

    def test_balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_get(self):
        """Test case for balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_get

        Indicative period BMU cashflows by settlement date (EBOCF)  # noqa: E501
        """
        pass

    def test_balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_settlement_period_get

        Indicative period BMU cashflows by settlement period (EBOCF)  # noqa: E501
        """
        pass

    def test_balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_get(self):
        """Test case for balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_get

        Indicative volumes by settlement date (DISPTAV)  # noqa: E501
        """
        pass

    def test_balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_settlement_period_get

        Indicative volumes by settlement period (DISPTAV)  # noqa: E501
        """
        pass

    def test_balancing_settlement_market_depth_settlement_date_get(self):
        """Test case for balancing_settlement_market_depth_settlement_date_get

        Market depth by settlement date (IMBALNGC, BOD, DISEBSP, DISPTAV)  # noqa: E501
        """
        pass

    def test_balancing_settlement_market_depth_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_market_depth_settlement_date_settlement_period_get

        Market depth by settlement period (IMBALNGC, BOD, DISEBSP, DISPTAV)  # noqa: E501
        """
        pass

    def test_balancing_settlement_messages_settlement_date_get(self):
        """Test case for balancing_settlement_messages_settlement_date_get

        Settlement messages by settlement date (SMSG)  # noqa: E501
        """
        pass

    def test_balancing_settlement_messages_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_messages_settlement_date_settlement_period_get

        Settlement messages by settlement date and period (SMSG)  # noqa: E501
        """
        pass

    def test_balancing_settlement_stack_all_bid_offer_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_stack_all_bid_offer_settlement_date_settlement_period_get

        Settlement bid-offer stacks by settlement period (ISPSTACK)  # noqa: E501
        """
        pass

    def test_balancing_settlement_summary_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_summary_settlement_date_settlement_period_get

        Settlement calculation summary (ISPSTACK, DISEBSP, MID, NETBSAD)  # noqa: E501
        """
        pass

    def test_balancing_settlement_system_prices_settlement_date_get(self):
        """Test case for balancing_settlement_system_prices_settlement_date_get

        Settlement system prices by settlement date (DISEBSP)  # noqa: E501
        """
        pass

    def test_balancing_settlement_system_prices_settlement_date_settlement_period_get(self):
        """Test case for balancing_settlement_system_prices_settlement_date_settlement_period_get

        Settlement system prices by settlement date and period (DISEBSP)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
