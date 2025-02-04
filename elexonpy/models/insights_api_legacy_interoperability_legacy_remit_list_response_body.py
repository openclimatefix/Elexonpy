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

class InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody(object):
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
        'data_item': 'str',
        'legacy_remit_response_list': 'InsightsApiLegacyInteroperabilityLegacyRemitResponseList'
    }

    attribute_map = {
        'data_item': 'dataItem',
        'legacy_remit_response_list': 'legacyRemitResponseList'
    }

    def __init__(self, data_item=None, legacy_remit_response_list=None):  # noqa: E501
        """InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody - a model defined in Swagger"""  # noqa: E501
        self._data_item = None
        self._legacy_remit_response_list = None
        self.discriminator = None
        if data_item is not None:
            self.data_item = data_item
        if legacy_remit_response_list is not None:
            self.legacy_remit_response_list = legacy_remit_response_list

    @property
    def data_item(self):
        """Gets the data_item of this InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.  # noqa: E501


        :return: The data_item of this InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.  # noqa: E501
        :rtype: str
        """
        return self._data_item

    @data_item.setter
    def data_item(self, data_item):
        """Sets the data_item of this InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.


        :param data_item: The data_item of this InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.  # noqa: E501
        :type: str
        """

        self._data_item = data_item

    @property
    def legacy_remit_response_list(self):
        """Gets the legacy_remit_response_list of this InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.  # noqa: E501


        :return: The legacy_remit_response_list of this InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.  # noqa: E501
        :rtype: InsightsApiLegacyInteroperabilityLegacyRemitResponseList
        """
        return self._legacy_remit_response_list

    @legacy_remit_response_list.setter
    def legacy_remit_response_list(self, legacy_remit_response_list):
        """Sets the legacy_remit_response_list of this InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.


        :param legacy_remit_response_list: The legacy_remit_response_list of this InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.  # noqa: E501
        :type: InsightsApiLegacyInteroperabilityLegacyRemitResponseList
        """

        self._legacy_remit_response_list = legacy_remit_response_list

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
        if issubclass(InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody, dict):
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
        if not isinstance(other, InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
