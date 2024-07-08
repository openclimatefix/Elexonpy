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

class InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow(object):
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
        'serial_number': 'str',
        'file_creation_time': 'datetime',
        'trading_unit_type': 'str',
        'trading_unit_name': 'str',
        'settlement_date': 'date',
        'settlement_period': 'int',
        'settlement_run_type': 'str',
        'start_time': 'datetime',
        'delivery_mode': 'str',
        'import_volume': 'float',
        'export_volume': 'float',
        'net_volume': 'float'
    }

    attribute_map = {
        'dataset': 'dataset',
        'serial_number': 'serialNumber',
        'file_creation_time': 'fileCreationTime',
        'trading_unit_type': 'tradingUnitType',
        'trading_unit_name': 'tradingUnitName',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'settlement_run_type': 'settlementRunType',
        'start_time': 'startTime',
        'delivery_mode': 'deliveryMode',
        'import_volume': 'importVolume',
        'export_volume': 'exportVolume',
        'net_volume': 'netVolume'
    }

    def __init__(self, dataset=None, serial_number=None, file_creation_time=None, trading_unit_type=None, trading_unit_name=None, settlement_date=None, settlement_period=None, settlement_run_type=None, start_time=None, delivery_mode=None, import_volume=None, export_volume=None, net_volume=None):  # noqa: E501
        """InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._serial_number = None
        self._file_creation_time = None
        self._trading_unit_type = None
        self._trading_unit_name = None
        self._settlement_date = None
        self._settlement_period = None
        self._settlement_run_type = None
        self._start_time = None
        self._delivery_mode = None
        self._import_volume = None
        self._export_volume = None
        self._net_volume = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if serial_number is not None:
            self.serial_number = serial_number
        if file_creation_time is not None:
            self.file_creation_time = file_creation_time
        if trading_unit_type is not None:
            self.trading_unit_type = trading_unit_type
        if trading_unit_name is not None:
            self.trading_unit_name = trading_unit_name
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if settlement_run_type is not None:
            self.settlement_run_type = settlement_run_type
        if start_time is not None:
            self.start_time = start_time
        if delivery_mode is not None:
            self.delivery_mode = delivery_mode
        if import_volume is not None:
            self.import_volume = import_volume
        if export_volume is not None:
            self.export_volume = export_volume
        if net_volume is not None:
            self.net_volume = net_volume

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param dataset: The dataset of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def serial_number(self):
        """Gets the serial_number of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The serial_number of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param serial_number: The serial_number of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def file_creation_time(self):
        """Gets the file_creation_time of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The file_creation_time of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: datetime
        """
        return self._file_creation_time

    @file_creation_time.setter
    def file_creation_time(self, file_creation_time):
        """Sets the file_creation_time of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param file_creation_time: The file_creation_time of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: datetime
        """

        self._file_creation_time = file_creation_time

    @property
    def trading_unit_type(self):
        """Gets the trading_unit_type of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The trading_unit_type of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._trading_unit_type

    @trading_unit_type.setter
    def trading_unit_type(self, trading_unit_type):
        """Sets the trading_unit_type of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param trading_unit_type: The trading_unit_type of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: str
        """

        self._trading_unit_type = trading_unit_type

    @property
    def trading_unit_name(self):
        """Gets the trading_unit_name of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The trading_unit_name of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._trading_unit_name

    @trading_unit_name.setter
    def trading_unit_name(self, trading_unit_name):
        """Sets the trading_unit_name of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param trading_unit_name: The trading_unit_name of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: str
        """

        self._trading_unit_name = trading_unit_name

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def settlement_run_type(self):
        """Gets the settlement_run_type of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The settlement_run_type of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._settlement_run_type

    @settlement_run_type.setter
    def settlement_run_type(self, settlement_run_type):
        """Sets the settlement_run_type of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param settlement_run_type: The settlement_run_type of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: str
        """

        self._settlement_run_type = settlement_run_type

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param start_time: The start_time of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def delivery_mode(self):
        """Gets the delivery_mode of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The delivery_mode of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._delivery_mode

    @delivery_mode.setter
    def delivery_mode(self, delivery_mode):
        """Sets the delivery_mode of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param delivery_mode: The delivery_mode of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: str
        """

        self._delivery_mode = delivery_mode

    @property
    def import_volume(self):
        """Gets the import_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The import_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: float
        """
        return self._import_volume

    @import_volume.setter
    def import_volume(self, import_volume):
        """Sets the import_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param import_volume: The import_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: float
        """

        self._import_volume = import_volume

    @property
    def export_volume(self):
        """Gets the export_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The export_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: float
        """
        return self._export_volume

    @export_volume.setter
    def export_volume(self, export_volume):
        """Sets the export_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param export_volume: The export_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: float
        """

        self._export_volume = export_volume

    @property
    def net_volume(self):
        """Gets the net_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501


        :return: The net_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :rtype: float
        """
        return self._net_volume

    @net_volume.setter
    def net_volume(self, net_volume):
        """Sets the net_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.


        :param net_volume: The net_volume of this InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.  # noqa: E501
        :type: float
        """

        self._net_volume = net_volume

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
        if issubclass(InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other