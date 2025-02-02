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

class InsightsApiLegacyInteroperabilityLegacyRemitListResponse(object):
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
        'legacy_remit_list_metadata': 'InsightsApiLegacyInteroperabilityLegacyRemitListMetadata',
        'legacy_remit_list_response_body': 'InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody'
    }

    attribute_map = {
        'legacy_remit_list_metadata': 'legacyRemitListMetadata',
        'legacy_remit_list_response_body': 'legacyRemitListResponseBody'
    }

    def __init__(self, legacy_remit_list_metadata=None, legacy_remit_list_response_body=None):  # noqa: E501
        """InsightsApiLegacyInteroperabilityLegacyRemitListResponse - a model defined in Swagger"""  # noqa: E501
        self._legacy_remit_list_metadata = None
        self._legacy_remit_list_response_body = None
        self.discriminator = None
        if legacy_remit_list_metadata is not None:
            self.legacy_remit_list_metadata = legacy_remit_list_metadata
        if legacy_remit_list_response_body is not None:
            self.legacy_remit_list_response_body = legacy_remit_list_response_body

    @property
    def legacy_remit_list_metadata(self):
        """Gets the legacy_remit_list_metadata of this InsightsApiLegacyInteroperabilityLegacyRemitListResponse.  # noqa: E501


        :return: The legacy_remit_list_metadata of this InsightsApiLegacyInteroperabilityLegacyRemitListResponse.  # noqa: E501
        :rtype: InsightsApiLegacyInteroperabilityLegacyRemitListMetadata
        """
        return self._legacy_remit_list_metadata

    @legacy_remit_list_metadata.setter
    def legacy_remit_list_metadata(self, legacy_remit_list_metadata):
        """Sets the legacy_remit_list_metadata of this InsightsApiLegacyInteroperabilityLegacyRemitListResponse.


        :param legacy_remit_list_metadata: The legacy_remit_list_metadata of this InsightsApiLegacyInteroperabilityLegacyRemitListResponse.  # noqa: E501
        :type: InsightsApiLegacyInteroperabilityLegacyRemitListMetadata
        """

        self._legacy_remit_list_metadata = legacy_remit_list_metadata

    @property
    def legacy_remit_list_response_body(self):
        """Gets the legacy_remit_list_response_body of this InsightsApiLegacyInteroperabilityLegacyRemitListResponse.  # noqa: E501


        :return: The legacy_remit_list_response_body of this InsightsApiLegacyInteroperabilityLegacyRemitListResponse.  # noqa: E501
        :rtype: InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody
        """
        return self._legacy_remit_list_response_body

    @legacy_remit_list_response_body.setter
    def legacy_remit_list_response_body(self, legacy_remit_list_response_body):
        """Sets the legacy_remit_list_response_body of this InsightsApiLegacyInteroperabilityLegacyRemitListResponse.


        :param legacy_remit_list_response_body: The legacy_remit_list_response_body of this InsightsApiLegacyInteroperabilityLegacyRemitListResponse.  # noqa: E501
        :type: InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody
        """

        self._legacy_remit_list_response_body = legacy_remit_list_response_body

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
        if issubclass(InsightsApiLegacyInteroperabilityLegacyRemitListResponse, dict):
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
        if not isinstance(other, InsightsApiLegacyInteroperabilityLegacyRemitListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
