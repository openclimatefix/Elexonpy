# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'settlement_date': 'date',
        'settlement_period': 'int',
        'bm_unit': 'str',
        'national_grid_bm_unit': 'str',
        'acceptance_number': 'int',
        'acceptance_time': 'datetime',
        'bid_price': 'float',
        'offer_price': 'float',
        'bid_offer_pair_id': 'int'
    }

    attribute_map = {
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'bm_unit': 'bmUnit',
        'national_grid_bm_unit': 'nationalGridBmUnit',
        'acceptance_number': 'acceptanceNumber',
        'acceptance_time': 'acceptanceTime',
        'bid_price': 'bidPrice',
        'offer_price': 'offerPrice',
        'bid_offer_pair_id': 'bidOfferPairId'
    }

    def __init__(self, settlement_date=None, settlement_period=None, bm_unit=None, national_grid_bm_unit=None, acceptance_number=None, acceptance_time=None, bid_price=None, offer_price=None, bid_offer_pair_id=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse - a model defined in Swagger"""  # noqa: E501
        self._settlement_date = None
        self._settlement_period = None
        self._bm_unit = None
        self._national_grid_bm_unit = None
        self._acceptance_number = None
        self._acceptance_time = None
        self._bid_price = None
        self._offer_price = None
        self._bid_offer_pair_id = None
        self.discriminator = None
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if bm_unit is not None:
            self.bm_unit = bm_unit
        if national_grid_bm_unit is not None:
            self.national_grid_bm_unit = national_grid_bm_unit
        if acceptance_number is not None:
            self.acceptance_number = acceptance_number
        if acceptance_time is not None:
            self.acceptance_time = acceptance_time
        if bid_price is not None:
            self.bid_price = bid_price
        if offer_price is not None:
            self.offer_price = offer_price
        if bid_offer_pair_id is not None:
            self.bid_offer_pair_id = bid_offer_pair_id

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def bm_unit(self):
        """Gets the bm_unit of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The bm_unit of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit

    @bm_unit.setter
    def bm_unit(self, bm_unit):
        """Sets the bm_unit of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param bm_unit: The bm_unit of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: str
        """

        self._bm_unit = bm_unit

    @property
    def national_grid_bm_unit(self):
        """Gets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._national_grid_bm_unit

    @national_grid_bm_unit.setter
    def national_grid_bm_unit(self, national_grid_bm_unit):
        """Sets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param national_grid_bm_unit: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: str
        """

        self._national_grid_bm_unit = national_grid_bm_unit

    @property
    def acceptance_number(self):
        """Gets the acceptance_number of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The acceptance_number of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._acceptance_number

    @acceptance_number.setter
    def acceptance_number(self, acceptance_number):
        """Sets the acceptance_number of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param acceptance_number: The acceptance_number of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: int
        """

        self._acceptance_number = acceptance_number

    @property
    def acceptance_time(self):
        """Gets the acceptance_time of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The acceptance_time of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._acceptance_time

    @acceptance_time.setter
    def acceptance_time(self, acceptance_time):
        """Sets the acceptance_time of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param acceptance_time: The acceptance_time of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: datetime
        """

        self._acceptance_time = acceptance_time

    @property
    def bid_price(self):
        """Gets the bid_price of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The bid_price of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._bid_price

    @bid_price.setter
    def bid_price(self, bid_price):
        """Sets the bid_price of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param bid_price: The bid_price of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: float
        """

        self._bid_price = bid_price

    @property
    def offer_price(self):
        """Gets the offer_price of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The offer_price of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._offer_price

    @offer_price.setter
    def offer_price(self, offer_price):
        """Sets the offer_price of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param offer_price: The offer_price of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: float
        """

        self._offer_price = offer_price

    @property
    def bid_offer_pair_id(self):
        """Gets the bid_offer_pair_id of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501


        :return: The bid_offer_pair_id of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._bid_offer_pair_id

    @bid_offer_pair_id.setter
    def bid_offer_pair_id(self, bid_offer_pair_id):
        """Sets the bid_offer_pair_id of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.


        :param bid_offer_pair_id: The bid_offer_pair_id of this InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.  # noqa: E501
        :type: int
        """

        self._bid_offer_pair_id = bid_offer_pair_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value
        if issubclass(InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse, dict):
            for key, value in list(self.items()):
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
