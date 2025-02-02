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

class InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak(object):
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
        'publish_time': 'datetime',
        'start_time': 'datetime',
        'settlement_date': 'date',
        'settlement_period': 'int',
        'initial_transmission_system_demand_outturn': 'int'
    }

    attribute_map = {
        'publish_time': 'publishTime',
        'start_time': 'startTime',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'initial_transmission_system_demand_outturn': 'initialTransmissionSystemDemandOutturn'
    }

    def __init__(self, publish_time=None, start_time=None, settlement_date=None, settlement_period=None, initial_transmission_system_demand_outturn=None):  # noqa: E501
        """InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak - a model defined in Swagger"""  # noqa: E501
        self._publish_time = None
        self._start_time = None
        self._settlement_date = None
        self._settlement_period = None
        self._initial_transmission_system_demand_outturn = None
        self.discriminator = None
        if publish_time is not None:
            self.publish_time = publish_time
        if start_time is not None:
            self.start_time = start_time
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if initial_transmission_system_demand_outturn is not None:
            self.initial_transmission_system_demand_outturn = initial_transmission_system_demand_outturn

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.


        :param start_time: The start_time of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def initial_transmission_system_demand_outturn(self):
        """Gets the initial_transmission_system_demand_outturn of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501


        :return: The initial_transmission_system_demand_outturn of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :rtype: int
        """
        return self._initial_transmission_system_demand_outturn

    @initial_transmission_system_demand_outturn.setter
    def initial_transmission_system_demand_outturn(self, initial_transmission_system_demand_outturn):
        """Sets the initial_transmission_system_demand_outturn of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.


        :param initial_transmission_system_demand_outturn: The initial_transmission_system_demand_outturn of this InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.  # noqa: E501
        :type: int
        """

        self._initial_transmission_system_demand_outturn = initial_transmission_system_demand_outturn

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
        if issubclass(InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
