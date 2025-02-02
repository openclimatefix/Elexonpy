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

class InsightsApiModelsResponsesTransparencyActualGenerationValue(object):
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
        'business_type': 'str',
        'psr_type': 'str',
        'quantity': 'float'
    }

    attribute_map = {
        'business_type': 'businessType',
        'psr_type': 'psrType',
        'quantity': 'quantity'
    }

    def __init__(self, business_type=None, psr_type=None, quantity=None):  # noqa: E501
        """InsightsApiModelsResponsesTransparencyActualGenerationValue - a model defined in Swagger"""  # noqa: E501
        self._business_type = None
        self._psr_type = None
        self._quantity = None
        self.discriminator = None
        if business_type is not None:
            self.business_type = business_type
        if psr_type is not None:
            self.psr_type = psr_type
        if quantity is not None:
            self.quantity = quantity

    @property
    def business_type(self):
        """Gets the business_type of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501


        :return: The business_type of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this InsightsApiModelsResponsesTransparencyActualGenerationValue.


        :param business_type: The business_type of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501
        :type: str
        """

        self._business_type = business_type

    @property
    def psr_type(self):
        """Gets the psr_type of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501


        :return: The psr_type of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501
        :rtype: str
        """
        return self._psr_type

    @psr_type.setter
    def psr_type(self, psr_type):
        """Sets the psr_type of this InsightsApiModelsResponsesTransparencyActualGenerationValue.


        :param psr_type: The psr_type of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501
        :type: str
        """

        self._psr_type = psr_type

    @property
    def quantity(self):
        """Gets the quantity of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501


        :return: The quantity of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InsightsApiModelsResponsesTransparencyActualGenerationValue.


        :param quantity: The quantity of this InsightsApiModelsResponsesTransparencyActualGenerationValue.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

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
        if issubclass(InsightsApiModelsResponsesTransparencyActualGenerationValue, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesTransparencyActualGenerationValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
