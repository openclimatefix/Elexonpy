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

class InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly(object):
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
        'year': 'int',
        'week': 'int',
        'demand': 'int'
    }

    attribute_map = {
        'dataset': 'dataset',
        'publish_time': 'publishTime',
        'year': 'year',
        'week': 'week',
        'demand': 'demand'
    }

    def __init__(self, dataset=None, publish_time=None, year=None, week=None, demand=None):  # noqa: E501
        """InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._publish_time = None
        self._year = None
        self._week = None
        self._demand = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if publish_time is not None:
            self.publish_time = publish_time
        if year is not None:
            self.year = year
        if week is not None:
            self.week = week
        if demand is not None:
            self.demand = demand

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.


        :param dataset: The dataset of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def year(self):
        """Gets the year of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501


        :return: The year of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.


        :param year: The year of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def week(self):
        """Gets the week of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501


        :return: The week of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.


        :param week: The week of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def demand(self):
        """Gets the demand of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501


        :return: The demand of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
        :rtype: int
        """
        return self._demand

    @demand.setter
    def demand(self, demand):
        """Sets the demand of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.


        :param demand: The demand of this InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.  # noqa: E501
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
        if issubclass(InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
