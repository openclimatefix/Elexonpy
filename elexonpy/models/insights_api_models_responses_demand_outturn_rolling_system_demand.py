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

class InsightsApiModelsResponsesDemandOutturnRollingSystemDemand(object):
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
        'record_type': 'str',
        'start_time': 'datetime',
        'demand': 'int'
    }

    attribute_map = {
        'record_type': 'recordType',
        'start_time': 'startTime',
        'demand': 'demand'
    }

    def __init__(self, record_type=None, start_time=None, demand=None):  # noqa: E501
        """InsightsApiModelsResponsesDemandOutturnRollingSystemDemand - a model defined in Swagger"""  # noqa: E501
        self._record_type = None
        self._start_time = None
        self._demand = None
        self.discriminator = None
        if record_type is not None:
            self.record_type = record_type
        if start_time is not None:
            self.start_time = start_time
        if demand is not None:
            self.demand = demand

    @property
    def record_type(self):
        """Gets the record_type of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501


        :return: The record_type of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.


        :param record_type: The record_type of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501
        :type: str
        """

        self._record_type = record_type

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.


        :param start_time: The start_time of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def demand(self):
        """Gets the demand of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501


        :return: The demand of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501
        :rtype: int
        """
        return self._demand

    @demand.setter
    def demand(self, demand):
        """Sets the demand of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.


        :param demand: The demand of this InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.  # noqa: E501
        :type: int
        """

        self._demand = demand

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
        if issubclass(InsightsApiModelsResponsesDemandOutturnRollingSystemDemand, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesDemandOutturnRollingSystemDemand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
