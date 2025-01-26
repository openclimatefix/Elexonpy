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

class InsightsApiModelsResponsesGenerationGenerationByFuelType(object):
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
        'dataset': 'str',
        'fuel_type': 'str',
        'current_usage': 'int',
        'current_percentage': 'float',
        'half_hour_usage': 'int',
        'half_hour_percentage': 'float',
        'twenty_four_hour_usage': 'int',
        'twenty_four_hour_percentage': 'float'
    }

    attribute_map = {
        'dataset': 'dataset',
        'fuel_type': 'fuelType',
        'current_usage': 'currentUsage',
        'current_percentage': 'currentPercentage',
        'half_hour_usage': 'halfHourUsage',
        'half_hour_percentage': 'halfHourPercentage',
        'twenty_four_hour_usage': 'twentyFourHourUsage',
        'twenty_four_hour_percentage': 'twentyFourHourPercentage'
    }

    def __init__(self, dataset=None, fuel_type=None, current_usage=None, current_percentage=None, half_hour_usage=None, half_hour_percentage=None, twenty_four_hour_usage=None, twenty_four_hour_percentage=None):  # noqa: E501
        """InsightsApiModelsResponsesGenerationGenerationByFuelType - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._fuel_type = None
        self._current_usage = None
        self._current_percentage = None
        self._half_hour_usage = None
        self._half_hour_percentage = None
        self._twenty_four_hour_usage = None
        self._twenty_four_hour_percentage = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if current_usage is not None:
            self.current_usage = current_usage
        if current_percentage is not None:
            self.current_percentage = current_percentage
        if half_hour_usage is not None:
            self.half_hour_usage = half_hour_usage
        if half_hour_percentage is not None:
            self.half_hour_percentage = half_hour_percentage
        if twenty_four_hour_usage is not None:
            self.twenty_four_hour_usage = twenty_four_hour_usage
        if twenty_four_hour_percentage is not None:
            self.twenty_four_hour_percentage = twenty_four_hour_percentage

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesGenerationGenerationByFuelType.


        :param dataset: The dataset of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def fuel_type(self):
        """Gets the fuel_type of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501


        :return: The fuel_type of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Sets the fuel_type of this InsightsApiModelsResponsesGenerationGenerationByFuelType.


        :param fuel_type: The fuel_type of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :type: str
        """

        self._fuel_type = fuel_type

    @property
    def current_usage(self):
        """Gets the current_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501


        :return: The current_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :rtype: int
        """
        return self._current_usage

    @current_usage.setter
    def current_usage(self, current_usage):
        """Sets the current_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.


        :param current_usage: The current_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :type: int
        """

        self._current_usage = current_usage

    @property
    def current_percentage(self):
        """Gets the current_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501


        :return: The current_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :rtype: float
        """
        return self._current_percentage

    @current_percentage.setter
    def current_percentage(self, current_percentage):
        """Sets the current_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.


        :param current_percentage: The current_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :type: float
        """

        self._current_percentage = current_percentage

    @property
    def half_hour_usage(self):
        """Gets the half_hour_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501


        :return: The half_hour_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :rtype: int
        """
        return self._half_hour_usage

    @half_hour_usage.setter
    def half_hour_usage(self, half_hour_usage):
        """Sets the half_hour_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.


        :param half_hour_usage: The half_hour_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :type: int
        """

        self._half_hour_usage = half_hour_usage

    @property
    def half_hour_percentage(self):
        """Gets the half_hour_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501


        :return: The half_hour_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :rtype: float
        """
        return self._half_hour_percentage

    @half_hour_percentage.setter
    def half_hour_percentage(self, half_hour_percentage):
        """Sets the half_hour_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.


        :param half_hour_percentage: The half_hour_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :type: float
        """

        self._half_hour_percentage = half_hour_percentage

    @property
    def twenty_four_hour_usage(self):
        """Gets the twenty_four_hour_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501


        :return: The twenty_four_hour_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :rtype: int
        """
        return self._twenty_four_hour_usage

    @twenty_four_hour_usage.setter
    def twenty_four_hour_usage(self, twenty_four_hour_usage):
        """Sets the twenty_four_hour_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.


        :param twenty_four_hour_usage: The twenty_four_hour_usage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :type: int
        """

        self._twenty_four_hour_usage = twenty_four_hour_usage

    @property
    def twenty_four_hour_percentage(self):
        """Gets the twenty_four_hour_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501


        :return: The twenty_four_hour_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :rtype: float
        """
        return self._twenty_four_hour_percentage

    @twenty_four_hour_percentage.setter
    def twenty_four_hour_percentage(self, twenty_four_hour_percentage):
        """Sets the twenty_four_hour_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.


        :param twenty_four_hour_percentage: The twenty_four_hour_percentage of this InsightsApiModelsResponsesGenerationGenerationByFuelType.  # noqa: E501
        :type: float
        """

        self._twenty_four_hour_percentage = twenty_four_hour_percentage

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
        if issubclass(InsightsApiModelsResponsesGenerationGenerationByFuelType, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesGenerationGenerationByFuelType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
