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

class InsightsApiModelsResponsesGenerationOutturnGenerationValue(object):
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
        'fuel_type': 'str',
        'generation': 'int'
    }

    attribute_map = {
        'fuel_type': 'fuelType',
        'generation': 'generation'
    }

    def __init__(self, fuel_type=None, generation=None):  # noqa: E501
        """InsightsApiModelsResponsesGenerationOutturnGenerationValue - a model defined in Swagger"""  # noqa: E501
        self._fuel_type = None
        self._generation = None
        self.discriminator = None
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if generation is not None:
            self.generation = generation

    @property
    def fuel_type(self):
        """Gets the fuel_type of this InsightsApiModelsResponsesGenerationOutturnGenerationValue.  # noqa: E501


        :return: The fuel_type of this InsightsApiModelsResponsesGenerationOutturnGenerationValue.  # noqa: E501
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Sets the fuel_type of this InsightsApiModelsResponsesGenerationOutturnGenerationValue.


        :param fuel_type: The fuel_type of this InsightsApiModelsResponsesGenerationOutturnGenerationValue.  # noqa: E501
        :type: str
        """

        self._fuel_type = fuel_type

    @property
    def generation(self):
        """Gets the generation of this InsightsApiModelsResponsesGenerationOutturnGenerationValue.  # noqa: E501


        :return: The generation of this InsightsApiModelsResponsesGenerationOutturnGenerationValue.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this InsightsApiModelsResponsesGenerationOutturnGenerationValue.


        :param generation: The generation of this InsightsApiModelsResponsesGenerationOutturnGenerationValue.  # noqa: E501
        :type: int
        """

        self._generation = generation

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
        if issubclass(InsightsApiModelsResponsesGenerationOutturnGenerationValue, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesGenerationOutturnGenerationValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
