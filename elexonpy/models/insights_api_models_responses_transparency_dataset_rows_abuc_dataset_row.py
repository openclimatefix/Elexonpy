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

class InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow(object):
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
        'business_type': 'str',
        'psr_type': 'str',
        'market_agreement_type': 'str',
        'flow_direction': 'str',
        'settlement_date': 'date',
        'quantity': 'float'
    }

    attribute_map = {
        'dataset': 'dataset',
        'document_id': 'documentId',
        'document_revision_number': 'documentRevisionNumber',
        'publish_time': 'publishTime',
        'business_type': 'businessType',
        'psr_type': 'psrType',
        'market_agreement_type': 'marketAgreementType',
        'flow_direction': 'flowDirection',
        'settlement_date': 'settlementDate',
        'quantity': 'quantity'
    }

    def __init__(self, dataset=None, document_id=None, document_revision_number=None, publish_time=None, business_type=None, psr_type=None, market_agreement_type=None, flow_direction=None, settlement_date=None, quantity=None):  # noqa: E501
        """InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._document_id = None
        self._document_revision_number = None
        self._publish_time = None
        self._business_type = None
        self._psr_type = None
        self._market_agreement_type = None
        self._flow_direction = None
        self._settlement_date = None
        self._quantity = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if document_id is not None:
            self.document_id = document_id
        if document_revision_number is not None:
            self.document_revision_number = document_revision_number
        if publish_time is not None:
            self.publish_time = publish_time
        if business_type is not None:
            self.business_type = business_type
        if psr_type is not None:
            self.psr_type = psr_type
        if market_agreement_type is not None:
            self.market_agreement_type = market_agreement_type
        if flow_direction is not None:
            self.flow_direction = flow_direction
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if quantity is not None:
            self.quantity = quantity

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param dataset: The dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def document_id(self):
        """Gets the document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param document_id: The document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_revision_number(self):
        """Gets the document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: int
        """
        return self._document_revision_number

    @document_revision_number.setter
    def document_revision_number(self, document_revision_number):
        """Sets the document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param document_revision_number: The document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: int
        """

        self._document_revision_number = document_revision_number

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def business_type(self):
        """Gets the business_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The business_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param business_type: The business_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: str
        """

        self._business_type = business_type

    @property
    def psr_type(self):
        """Gets the psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._psr_type

    @psr_type.setter
    def psr_type(self, psr_type):
        """Sets the psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param psr_type: The psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: str
        """

        self._psr_type = psr_type

    @property
    def market_agreement_type(self):
        """Gets the market_agreement_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The market_agreement_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._market_agreement_type

    @market_agreement_type.setter
    def market_agreement_type(self, market_agreement_type):
        """Sets the market_agreement_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param market_agreement_type: The market_agreement_type of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: str
        """

        self._market_agreement_type = market_agreement_type

    @property
    def flow_direction(self):
        """Gets the flow_direction of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The flow_direction of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._flow_direction

    @flow_direction.setter
    def flow_direction(self, flow_direction):
        """Sets the flow_direction of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param flow_direction: The flow_direction of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: str
        """

        self._flow_direction = flow_direction

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def quantity(self):
        """Gets the quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501


        :return: The quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.


        :param quantity: The quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

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
        if issubclass(InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
