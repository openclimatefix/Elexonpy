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

class InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData(object):
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
        'settlement_date': 'date',
        'settlement_period': 'int',
        'time': 'datetime',
        'period_max': 'int',
        'national_grid_bm_unit': 'str',
        'bm_unit': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'time': 'time',
        'period_max': 'periodMax',
        'national_grid_bm_unit': 'nationalGridBmUnit',
        'bm_unit': 'bmUnit'
    }

    def __init__(self, dataset=None, settlement_date=None, settlement_period=None, time=None, period_max=None, national_grid_bm_unit=None, bm_unit=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._settlement_date = None
        self._settlement_period = None
        self._time = None
        self._period_max = None
        self._national_grid_bm_unit = None
        self._bm_unit = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if time is not None:
            self.time = time
        if period_max is not None:
            self.period_max = period_max
        if national_grid_bm_unit is not None:
            self.national_grid_bm_unit = national_grid_bm_unit
        if bm_unit is not None:
            self.bm_unit = bm_unit

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.


        :param dataset: The dataset of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def time(self):
        """Gets the time of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501


        :return: The time of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.


        :param time: The time of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def period_max(self):
        """Gets the period_max of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501


        :return: The period_max of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :rtype: int
        """
        return self._period_max

    @period_max.setter
    def period_max(self, period_max):
        """Sets the period_max of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.


        :param period_max: The period_max of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :type: int
        """

        self._period_max = period_max

    @property
    def national_grid_bm_unit(self):
        """Gets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501


        :return: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :rtype: str
        """
        return self._national_grid_bm_unit

    @national_grid_bm_unit.setter
    def national_grid_bm_unit(self, national_grid_bm_unit):
        """Sets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.


        :param national_grid_bm_unit: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :type: str
        """

        self._national_grid_bm_unit = national_grid_bm_unit

    @property
    def bm_unit(self):
        """Gets the bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501


        :return: The bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit

    @bm_unit.setter
    def bm_unit(self, bm_unit):
        """Sets the bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.


        :param bm_unit: The bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.  # noqa: E501
        :type: str
        """

        self._bm_unit = bm_unit

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
        if issubclass(InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
