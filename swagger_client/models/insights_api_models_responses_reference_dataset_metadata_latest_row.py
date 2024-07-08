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

class InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow(object):
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
        'last_updated': 'datetime'
    }

    attribute_map = {
        'dataset': 'dataset',
        'last_updated': 'lastUpdated'
    }

    def __init__(self, dataset=None, last_updated=None):  # noqa: E501
        """InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._last_updated = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.


        :param dataset: The dataset of this InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def last_updated(self):
        """Gets the last_updated of this InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.  # noqa: E501


        :return: The last_updated of this InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.


        :param last_updated: The last_updated of this InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if issubclass(InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
