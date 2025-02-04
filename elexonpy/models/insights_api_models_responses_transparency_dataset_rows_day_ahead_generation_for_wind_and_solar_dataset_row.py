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

class InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow(object):
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
        'document_id': 'str',
        'document_revision_number': 'int',
        'publish_time': 'datetime',
        'process_type': 'str',
        'business_type': 'str',
        'psr_type': 'str',
        'quantity': 'float',
        'start_time': 'datetime',
        'settlement_date': 'date',
        'settlement_period': 'int'
    }

    attribute_map = {
        'dataset': 'dataset',
        'document_id': 'documentId',
        'document_revision_number': 'documentRevisionNumber',
        'publish_time': 'publishTime',
        'process_type': 'processType',
        'business_type': 'businessType',
        'psr_type': 'psrType',
        'quantity': 'quantity',
        'start_time': 'startTime',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod'
    }

    def __init__(self, dataset=None, document_id=None, document_revision_number=None, publish_time=None, process_type=None, business_type=None, psr_type=None, quantity=None, start_time=None, settlement_date=None, settlement_period=None):  # noqa: E501
        """InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._document_id = None
        self._document_revision_number = None
        self._publish_time = None
        self._process_type = None
        self._business_type = None
        self._psr_type = None
        self._quantity = None
        self._start_time = None
        self._settlement_date = None
        self._settlement_period = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if document_id is not None:
            self.document_id = document_id
        if document_revision_number is not None:
            self.document_revision_number = document_revision_number
        if publish_time is not None:
            self.publish_time = publish_time
        if process_type is not None:
            self.process_type = process_type
        if business_type is not None:
            self.business_type = business_type
        if psr_type is not None:
            self.psr_type = psr_type
        if quantity is not None:
            self.quantity = quantity
        if start_time is not None:
            self.start_time = start_time
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param dataset: The dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def document_id(self):
        """Gets the document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param document_id: The document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_revision_number(self):
        """Gets the document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: int
        """
        return self._document_revision_number

    @document_revision_number.setter
    def document_revision_number(self, document_revision_number):
        """Sets the document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param document_revision_number: The document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: int
        """

        self._document_revision_number = document_revision_number

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def process_type(self):
        """Gets the process_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The process_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        """Sets the process_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param process_type: The process_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: str
        """

        self._process_type = process_type

    @property
    def business_type(self):
        """Gets the business_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The business_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param business_type: The business_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: str
        """

        self._business_type = business_type

    @property
    def psr_type(self):
        """Gets the psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._psr_type

    @psr_type.setter
    def psr_type(self, psr_type):
        """Sets the psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param psr_type: The psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: str
        """

        self._psr_type = psr_type

    @property
    def quantity(self):
        """Gets the quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param quantity: The quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param start_time: The start_time of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

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
        if issubclass(InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
