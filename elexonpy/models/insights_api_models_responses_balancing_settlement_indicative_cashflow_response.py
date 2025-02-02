# coding: utf-8

"""
    Insights API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse(object):
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
        'start_time': 'datetime',
        'created_date_time': 'datetime',
        'bm_unit': 'str',
        'bm_unit_type': 'str',
        'lead_party_name': 'str',
        'national_grid_bm_unit': 'str',
        'bid_offer_pair_cashflows': 'InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs',
        'total_cashflow': 'float'
    }

    attribute_map = {
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'start_time': 'startTime',
        'created_date_time': 'createdDateTime',
        'bm_unit': 'bmUnit',
        'bm_unit_type': 'bmUnitType',
        'lead_party_name': 'leadPartyName',
        'national_grid_bm_unit': 'nationalGridBmUnit',
        'bid_offer_pair_cashflows': 'bidOfferPairCashflows',
        'total_cashflow': 'totalCashflow'
    }

    def __init__(self, settlement_date=None, settlement_period=None, start_time=None, created_date_time=None, bm_unit=None, bm_unit_type=None, lead_party_name=None, national_grid_bm_unit=None, bid_offer_pair_cashflows=None, total_cashflow=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse - a model defined in Swagger"""  # noqa: E501
        self._settlement_date = None
        self._settlement_period = None
        self._start_time = None
        self._created_date_time = None
        self._bm_unit = None
        self._bm_unit_type = None
        self._lead_party_name = None
        self._national_grid_bm_unit = None
        self._bid_offer_pair_cashflows = None
        self._total_cashflow = None
        self.discriminator = None
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if start_time is not None:
            self.start_time = start_time
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if bm_unit is not None:
            self.bm_unit = bm_unit
        if bm_unit_type is not None:
            self.bm_unit_type = bm_unit_type
        if lead_party_name is not None:
            self.lead_party_name = lead_party_name
        if national_grid_bm_unit is not None:
            self.national_grid_bm_unit = national_grid_bm_unit
        if bid_offer_pair_cashflows is not None:
            self.bid_offer_pair_cashflows = bid_offer_pair_cashflows
        if total_cashflow is not None:
            self.total_cashflow = total_cashflow

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param start_time: The start_time of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def created_date_time(self):
        """Gets the created_date_time of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The created_date_time of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param created_date_time: The created_date_time of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

    @property
    def bm_unit(self):
        """Gets the bm_unit of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The bm_unit of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit

    @bm_unit.setter
    def bm_unit(self, bm_unit):
        """Sets the bm_unit of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param bm_unit: The bm_unit of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: str
        """

        self._bm_unit = bm_unit

    @property
    def bm_unit_type(self):
        """Gets the bm_unit_type of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The bm_unit_type of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit_type

    @bm_unit_type.setter
    def bm_unit_type(self, bm_unit_type):
        """Sets the bm_unit_type of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param bm_unit_type: The bm_unit_type of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: str
        """

        self._bm_unit_type = bm_unit_type

    @property
    def lead_party_name(self):
        """Gets the lead_party_name of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The lead_party_name of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: str
        """
        return self._lead_party_name

    @lead_party_name.setter
    def lead_party_name(self, lead_party_name):
        """Sets the lead_party_name of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param lead_party_name: The lead_party_name of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: str
        """

        self._lead_party_name = lead_party_name

    @property
    def national_grid_bm_unit(self):
        """Gets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: str
        """
        return self._national_grid_bm_unit

    @national_grid_bm_unit.setter
    def national_grid_bm_unit(self, national_grid_bm_unit):
        """Sets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param national_grid_bm_unit: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: str
        """

        self._national_grid_bm_unit = national_grid_bm_unit

    @property
    def bid_offer_pair_cashflows(self):
        """Gets the bid_offer_pair_cashflows of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The bid_offer_pair_cashflows of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs
        """
        return self._bid_offer_pair_cashflows

    @bid_offer_pair_cashflows.setter
    def bid_offer_pair_cashflows(self, bid_offer_pair_cashflows):
        """Sets the bid_offer_pair_cashflows of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param bid_offer_pair_cashflows: The bid_offer_pair_cashflows of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs
        """

        self._bid_offer_pair_cashflows = bid_offer_pair_cashflows

    @property
    def total_cashflow(self):
        """Gets the total_cashflow of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501


        :return: The total_cashflow of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_cashflow

    @total_cashflow.setter
    def total_cashflow(self, total_cashflow):
        """Sets the total_cashflow of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.


        :param total_cashflow: The total_cashflow of this InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.  # noqa: E501
        :type: float
        """

        self._total_cashflow = total_cashflow

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse, dict):
            for key, value in self.items():
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
        if not isinstance(other, InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
