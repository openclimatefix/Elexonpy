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

class InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData(object):
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
        'volume_max': 'int',
        'national_grid_bm_unit': 'str',
        'bm_unit': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'time': 'time',
        'volume_max': 'volumeMax',
        'national_grid_bm_unit': 'nationalGridBmUnit',
        'bm_unit': 'bmUnit'
    }

    def __init__(self, dataset=None, settlement_date=None, settlement_period=None, time=None, volume_max=None, national_grid_bm_unit=None, bm_unit=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._settlement_date = None
        self._settlement_period = None
        self._time = None
        self._volume_max = None
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
        if volume_max is not None:
            self.volume_max = volume_max
        if national_grid_bm_unit is not None:
            self.national_grid_bm_unit = national_grid_bm_unit
        if bm_unit is not None:
            self.bm_unit = bm_unit

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.


        :param dataset: The dataset of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def time(self):
        """Gets the time of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501


        :return: The time of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.


        :param time: The time of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def volume_max(self):
        """Gets the volume_max of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501


        :return: The volume_max of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :rtype: int
        """
        return self._volume_max

    @volume_max.setter
    def volume_max(self, volume_max):
        """Sets the volume_max of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.


        :param volume_max: The volume_max of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :type: int
        """

        self._volume_max = volume_max

    @property
    def national_grid_bm_unit(self):
        """Gets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501


        :return: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :rtype: str
        """
        return self._national_grid_bm_unit

    @national_grid_bm_unit.setter
    def national_grid_bm_unit(self, national_grid_bm_unit):
        """Sets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.


        :param national_grid_bm_unit: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :type: str
        """

        self._national_grid_bm_unit = national_grid_bm_unit

    @property
    def bm_unit(self):
        """Gets the bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501


        :return: The bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit

    @bm_unit.setter
    def bm_unit(self, bm_unit):
        """Sets the bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.


        :param bm_unit: The bm_unit of this InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.  # noqa: E501
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
        if issubclass(InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
