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

class InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl(object):
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
        'id': 'int',
        'mrid': 'str',
        'revision_number': 'int',
        'created_time': 'datetime',
        'publish_time': 'datetime',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'mrid': 'mrid',
        'revision_number': 'revisionNumber',
        'created_time': 'createdTime',
        'publish_time': 'publishTime',
        'url': 'url'
    }

    def __init__(self, id=None, mrid=None, revision_number=None, created_time=None, publish_time=None, url=None):  # noqa: E501
        """InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._mrid = None
        self._revision_number = None
        self._created_time = None
        self._publish_time = None
        self._url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if mrid is not None:
            self.mrid = mrid
        if revision_number is not None:
            self.revision_number = revision_number
        if created_time is not None:
            self.created_time = created_time
        if publish_time is not None:
            self.publish_time = publish_time
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501


        :return: The id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.


        :param id: The id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mrid(self):
        """Gets the mrid of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501


        :return: The mrid of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :rtype: str
        """
        return self._mrid

    @mrid.setter
    def mrid(self, mrid):
        """Sets the mrid of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.


        :param mrid: The mrid of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :type: str
        """

        self._mrid = mrid

    @property
    def revision_number(self):
        """Gets the revision_number of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501


        :return: The revision_number of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :rtype: int
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.


        :param revision_number: The revision_number of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :type: int
        """

        self._revision_number = revision_number

    @property
    def created_time(self):
        """Gets the created_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501


        :return: The created_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.


        :param created_time: The created_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def url(self):
        """Gets the url of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501


        :return: The url of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.


        :param url: The url of this InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
