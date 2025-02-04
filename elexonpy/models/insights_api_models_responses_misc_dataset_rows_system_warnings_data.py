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

class InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData(object):
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
        'publish_time': 'datetime',
        'warning_text': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'publish_time': 'publishTime',
        'warning_text': 'warningText'
    }

    def __init__(self, dataset=None, publish_time=None, warning_text=None):  # noqa: E501
        """InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._publish_time = None
        self._warning_text = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if publish_time is not None:
            self.publish_time = publish_time
        if warning_text is not None:
            self.warning_text = warning_text

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.


        :param dataset: The dataset of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def warning_text(self):
        """Gets the warning_text of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501


        :return: The warning_text of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501
        :rtype: str
        """
        return self._warning_text

    @warning_text.setter
    def warning_text(self, warning_text):
        """Sets the warning_text of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.


        :param warning_text: The warning_text of this InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.  # noqa: E501
        :type: str
        """

        self._warning_text = warning_text

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
        if issubclass(InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
