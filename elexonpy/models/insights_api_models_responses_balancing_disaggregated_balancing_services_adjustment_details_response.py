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

class InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse(object):
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
        'id': 'int',
        'cost': 'float',
        'volume': 'float',
        'price': 'float',
        'so_flag': 'bool',
        'stor_flag': 'bool',
        'party_id': 'str',
        'asset_id': 'str',
        'is_tendered': 'bool',
        'service': 'str'
    }

    attribute_map = {
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'start_time': 'startTime',
        'id': 'id',
        'cost': 'cost',
        'volume': 'volume',
        'price': 'price',
        'so_flag': 'soFlag',
        'stor_flag': 'storFlag',
        'party_id': 'partyId',
        'asset_id': 'assetId',
        'is_tendered': 'isTendered',
        'service': 'service'
    }

    def __init__(self, settlement_date=None, settlement_period=None, start_time=None, id=None, cost=None, volume=None, price=None, so_flag=None, stor_flag=None, party_id=None, asset_id=None, is_tendered=None, service=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse - a model defined in Swagger"""  # noqa: E501
        self._settlement_date = None
        self._settlement_period = None
        self._start_time = None
        self._id = None
        self._cost = None
        self._volume = None
        self._price = None
        self._so_flag = None
        self._stor_flag = None
        self._party_id = None
        self._asset_id = None
        self._is_tendered = None
        self._service = None
        self.discriminator = None
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if start_time is not None:
            self.start_time = start_time
        if id is not None:
            self.id = id
        if cost is not None:
            self.cost = cost
        if volume is not None:
            self.volume = volume
        if price is not None:
            self.price = price
        if so_flag is not None:
            self.so_flag = so_flag
        if stor_flag is not None:
            self.stor_flag = stor_flag
        if party_id is not None:
            self.party_id = party_id
        if asset_id is not None:
            self.asset_id = asset_id
        if is_tendered is not None:
            self.is_tendered = is_tendered
        if service is not None:
            self.service = service

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param start_time: The start_time of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def id(self):
        """Gets the id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param id: The id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def cost(self):
        """Gets the cost of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The cost of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param cost: The cost of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def volume(self):
        """Gets the volume of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The volume of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param volume: The volume of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: float
        """

        self._volume = volume

    @property
    def price(self):
        """Gets the price of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The price of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param price: The price of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def so_flag(self):
        """Gets the so_flag of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The so_flag of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._so_flag

    @so_flag.setter
    def so_flag(self, so_flag):
        """Sets the so_flag of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param so_flag: The so_flag of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: bool
        """

        self._so_flag = so_flag

    @property
    def stor_flag(self):
        """Gets the stor_flag of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The stor_flag of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._stor_flag

    @stor_flag.setter
    def stor_flag(self, stor_flag):
        """Sets the stor_flag of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param stor_flag: The stor_flag of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: bool
        """

        self._stor_flag = stor_flag

    @property
    def party_id(self):
        """Gets the party_id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The party_id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._party_id

    @party_id.setter
    def party_id(self, party_id):
        """Sets the party_id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param party_id: The party_id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: str
        """

        self._party_id = party_id

    @property
    def asset_id(self):
        """Gets the asset_id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The asset_id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param asset_id: The asset_id of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def is_tendered(self):
        """Gets the is_tendered of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The is_tendered of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_tendered

    @is_tendered.setter
    def is_tendered(self, is_tendered):
        """Sets the is_tendered of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param is_tendered: The is_tendered of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: bool
        """

        self._is_tendered = is_tendered

    @property
    def service(self):
        """Gets the service of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501


        :return: The service of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.


        :param service: The service of this InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.  # noqa: E501
        :type: str
        """

        self._service = service

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
        if issubclass(InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
