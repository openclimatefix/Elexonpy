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

class InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs(object):
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
        'negative1': 'float',
        'positive1': 'float',
        'negative2': 'float',
        'positive2': 'float',
        'negative3': 'float',
        'positive3': 'float',
        'negative4': 'float',
        'positive4': 'float',
        'negative5': 'float',
        'positive5': 'float',
        'negative6': 'float',
        'positive6': 'float'
    }

    attribute_map = {
        'negative1': 'negative1',
        'positive1': 'positive1',
        'negative2': 'negative2',
        'positive2': 'positive2',
        'negative3': 'negative3',
        'positive3': 'positive3',
        'negative4': 'negative4',
        'positive4': 'positive4',
        'negative5': 'negative5',
        'positive5': 'positive5',
        'negative6': 'negative6',
        'positive6': 'positive6'
    }

    def __init__(self, negative1=None, positive1=None, negative2=None, positive2=None, negative3=None, positive3=None, negative4=None, positive4=None, negative5=None, positive5=None, negative6=None, positive6=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs - a model defined in Swagger"""  # noqa: E501
        self._negative1 = None
        self._positive1 = None
        self._negative2 = None
        self._positive2 = None
        self._negative3 = None
        self._positive3 = None
        self._negative4 = None
        self._positive4 = None
        self._negative5 = None
        self._positive5 = None
        self._negative6 = None
        self._positive6 = None
        self.discriminator = None
        if negative1 is not None:
            self.negative1 = negative1
        if positive1 is not None:
            self.positive1 = positive1
        if negative2 is not None:
            self.negative2 = negative2
        if positive2 is not None:
            self.positive2 = positive2
        if negative3 is not None:
            self.negative3 = negative3
        if positive3 is not None:
            self.positive3 = positive3
        if negative4 is not None:
            self.negative4 = negative4
        if positive4 is not None:
            self.positive4 = positive4
        if negative5 is not None:
            self.negative5 = negative5
        if positive5 is not None:
            self.positive5 = positive5
        if negative6 is not None:
            self.negative6 = negative6
        if positive6 is not None:
            self.positive6 = positive6

    @property
    def negative1(self):
        """Gets the negative1 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The negative1 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._negative1

    @negative1.setter
    def negative1(self, negative1):
        """Sets the negative1 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param negative1: The negative1 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._negative1 = negative1

    @property
    def positive1(self):
        """Gets the positive1 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The positive1 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._positive1

    @positive1.setter
    def positive1(self, positive1):
        """Sets the positive1 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param positive1: The positive1 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._positive1 = positive1

    @property
    def negative2(self):
        """Gets the negative2 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The negative2 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._negative2

    @negative2.setter
    def negative2(self, negative2):
        """Sets the negative2 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param negative2: The negative2 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._negative2 = negative2

    @property
    def positive2(self):
        """Gets the positive2 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The positive2 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._positive2

    @positive2.setter
    def positive2(self, positive2):
        """Sets the positive2 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param positive2: The positive2 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._positive2 = positive2

    @property
    def negative3(self):
        """Gets the negative3 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The negative3 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._negative3

    @negative3.setter
    def negative3(self, negative3):
        """Sets the negative3 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param negative3: The negative3 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._negative3 = negative3

    @property
    def positive3(self):
        """Gets the positive3 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The positive3 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._positive3

    @positive3.setter
    def positive3(self, positive3):
        """Sets the positive3 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param positive3: The positive3 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._positive3 = positive3

    @property
    def negative4(self):
        """Gets the negative4 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The negative4 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._negative4

    @negative4.setter
    def negative4(self, negative4):
        """Sets the negative4 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param negative4: The negative4 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._negative4 = negative4

    @property
    def positive4(self):
        """Gets the positive4 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The positive4 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._positive4

    @positive4.setter
    def positive4(self, positive4):
        """Sets the positive4 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param positive4: The positive4 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._positive4 = positive4

    @property
    def negative5(self):
        """Gets the negative5 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The negative5 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._negative5

    @negative5.setter
    def negative5(self, negative5):
        """Sets the negative5 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param negative5: The negative5 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._negative5 = negative5

    @property
    def positive5(self):
        """Gets the positive5 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The positive5 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._positive5

    @positive5.setter
    def positive5(self, positive5):
        """Sets the positive5 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param positive5: The positive5 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._positive5 = positive5

    @property
    def negative6(self):
        """Gets the negative6 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The negative6 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._negative6

    @negative6.setter
    def negative6(self, negative6):
        """Sets the negative6 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param negative6: The negative6 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._negative6 = negative6

    @property
    def positive6(self):
        """Gets the positive6 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501


        :return: The positive6 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :rtype: float
        """
        return self._positive6

    @positive6.setter
    def positive6(self, positive6):
        """Sets the positive6 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.


        :param positive6: The positive6 of this InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.  # noqa: E501
        :type: float
        """

        self._positive6 = positive6

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
        if issubclass(InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
