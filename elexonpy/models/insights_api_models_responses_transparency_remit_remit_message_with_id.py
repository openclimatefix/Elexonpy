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

class InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId(object):
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
        'mrid': 'str',
        'revision_number': 'int',
        'publish_time': 'datetime',
        'created_time': 'datetime',
        'message_type': 'str',
        'message_heading': 'str',
        'event_type': 'str',
        'unavailability_type': 'str',
        'participant_id': 'str',
        'registration_code': 'str',
        'asset_id': 'str',
        'asset_type': 'str',
        'affected_unit': 'str',
        'affected_unit_eic': 'str',
        'affected_area': 'str',
        'bidding_zone': 'str',
        'fuel_type': 'str',
        'normal_capacity': 'float',
        'available_capacity': 'float',
        'unavailable_capacity': 'float',
        'event_status': 'str',
        'event_start_time': 'datetime',
        'event_end_time': 'datetime',
        'duration_uncertainty': 'str',
        'cause': 'str',
        'related_information': 'str',
        'outage_profile': 'list[InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData]',
        'id': 'int'
    }

    attribute_map = {
        'dataset': 'dataset',
        'mrid': 'mrid',
        'revision_number': 'revisionNumber',
        'publish_time': 'publishTime',
        'created_time': 'createdTime',
        'message_type': 'messageType',
        'message_heading': 'messageHeading',
        'event_type': 'eventType',
        'unavailability_type': 'unavailabilityType',
        'participant_id': 'participantId',
        'registration_code': 'registrationCode',
        'asset_id': 'assetId',
        'asset_type': 'assetType',
        'affected_unit': 'affectedUnit',
        'affected_unit_eic': 'affectedUnitEIC',
        'affected_area': 'affectedArea',
        'bidding_zone': 'biddingZone',
        'fuel_type': 'fuelType',
        'normal_capacity': 'normalCapacity',
        'available_capacity': 'availableCapacity',
        'unavailable_capacity': 'unavailableCapacity',
        'event_status': 'eventStatus',
        'event_start_time': 'eventStartTime',
        'event_end_time': 'eventEndTime',
        'duration_uncertainty': 'durationUncertainty',
        'cause': 'cause',
        'related_information': 'relatedInformation',
        'outage_profile': 'outageProfile',
        'id': 'id'
    }

    def __init__(self, dataset=None, mrid=None, revision_number=None, publish_time=None, created_time=None, message_type=None, message_heading=None, event_type=None, unavailability_type=None, participant_id=None, registration_code=None, asset_id=None, asset_type=None, affected_unit=None, affected_unit_eic=None, affected_area=None, bidding_zone=None, fuel_type=None, normal_capacity=None, available_capacity=None, unavailable_capacity=None, event_status=None, event_start_time=None, event_end_time=None, duration_uncertainty=None, cause=None, related_information=None, outage_profile=None, id=None):  # noqa: E501
        """InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._mrid = None
        self._revision_number = None
        self._publish_time = None
        self._created_time = None
        self._message_type = None
        self._message_heading = None
        self._event_type = None
        self._unavailability_type = None
        self._participant_id = None
        self._registration_code = None
        self._asset_id = None
        self._asset_type = None
        self._affected_unit = None
        self._affected_unit_eic = None
        self._affected_area = None
        self._bidding_zone = None
        self._fuel_type = None
        self._normal_capacity = None
        self._available_capacity = None
        self._unavailable_capacity = None
        self._event_status = None
        self._event_start_time = None
        self._event_end_time = None
        self._duration_uncertainty = None
        self._cause = None
        self._related_information = None
        self._outage_profile = None
        self._id = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if mrid is not None:
            self.mrid = mrid
        if revision_number is not None:
            self.revision_number = revision_number
        if publish_time is not None:
            self.publish_time = publish_time
        if created_time is not None:
            self.created_time = created_time
        if message_type is not None:
            self.message_type = message_type
        if message_heading is not None:
            self.message_heading = message_heading
        if event_type is not None:
            self.event_type = event_type
        if unavailability_type is not None:
            self.unavailability_type = unavailability_type
        if participant_id is not None:
            self.participant_id = participant_id
        if registration_code is not None:
            self.registration_code = registration_code
        if asset_id is not None:
            self.asset_id = asset_id
        if asset_type is not None:
            self.asset_type = asset_type
        if affected_unit is not None:
            self.affected_unit = affected_unit
        if affected_unit_eic is not None:
            self.affected_unit_eic = affected_unit_eic
        if affected_area is not None:
            self.affected_area = affected_area
        if bidding_zone is not None:
            self.bidding_zone = bidding_zone
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if normal_capacity is not None:
            self.normal_capacity = normal_capacity
        if available_capacity is not None:
            self.available_capacity = available_capacity
        if unavailable_capacity is not None:
            self.unavailable_capacity = unavailable_capacity
        if event_status is not None:
            self.event_status = event_status
        if event_start_time is not None:
            self.event_start_time = event_start_time
        if event_end_time is not None:
            self.event_end_time = event_end_time
        if duration_uncertainty is not None:
            self.duration_uncertainty = duration_uncertainty
        if cause is not None:
            self.cause = cause
        if related_information is not None:
            self.related_information = related_information
        if outage_profile is not None:
            self.outage_profile = outage_profile
        if id is not None:
            self.id = id

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param dataset: The dataset of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def mrid(self):
        """Gets the mrid of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The mrid of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._mrid

    @mrid.setter
    def mrid(self, mrid):
        """Sets the mrid of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param mrid: The mrid of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._mrid = mrid

    @property
    def revision_number(self):
        """Gets the revision_number of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The revision_number of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: int
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param revision_number: The revision_number of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: int
        """

        self._revision_number = revision_number

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def created_time(self):
        """Gets the created_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The created_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param created_time: The created_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def message_type(self):
        """Gets the message_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The message_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param message_type: The message_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._message_type = message_type

    @property
    def message_heading(self):
        """Gets the message_heading of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The message_heading of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._message_heading

    @message_heading.setter
    def message_heading(self, message_heading):
        """Sets the message_heading of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param message_heading: The message_heading of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._message_heading = message_heading

    @property
    def event_type(self):
        """Gets the event_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The event_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param event_type: The event_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def unavailability_type(self):
        """Gets the unavailability_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The unavailability_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._unavailability_type

    @unavailability_type.setter
    def unavailability_type(self, unavailability_type):
        """Sets the unavailability_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param unavailability_type: The unavailability_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._unavailability_type = unavailability_type

    @property
    def participant_id(self):
        """Gets the participant_id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The participant_id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param participant_id: The participant_id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._participant_id = participant_id

    @property
    def registration_code(self):
        """Gets the registration_code of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The registration_code of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._registration_code

    @registration_code.setter
    def registration_code(self, registration_code):
        """Sets the registration_code of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param registration_code: The registration_code of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._registration_code = registration_code

    @property
    def asset_id(self):
        """Gets the asset_id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The asset_id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param asset_id: The asset_id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def asset_type(self):
        """Gets the asset_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The asset_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param asset_type: The asset_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._asset_type = asset_type

    @property
    def affected_unit(self):
        """Gets the affected_unit of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The affected_unit of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._affected_unit

    @affected_unit.setter
    def affected_unit(self, affected_unit):
        """Sets the affected_unit of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param affected_unit: The affected_unit of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._affected_unit = affected_unit

    @property
    def affected_unit_eic(self):
        """Gets the affected_unit_eic of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The affected_unit_eic of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._affected_unit_eic

    @affected_unit_eic.setter
    def affected_unit_eic(self, affected_unit_eic):
        """Sets the affected_unit_eic of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param affected_unit_eic: The affected_unit_eic of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._affected_unit_eic = affected_unit_eic

    @property
    def affected_area(self):
        """Gets the affected_area of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The affected_area of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._affected_area

    @affected_area.setter
    def affected_area(self, affected_area):
        """Sets the affected_area of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param affected_area: The affected_area of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._affected_area = affected_area

    @property
    def bidding_zone(self):
        """Gets the bidding_zone of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The bidding_zone of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._bidding_zone

    @bidding_zone.setter
    def bidding_zone(self, bidding_zone):
        """Sets the bidding_zone of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param bidding_zone: The bidding_zone of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._bidding_zone = bidding_zone

    @property
    def fuel_type(self):
        """Gets the fuel_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The fuel_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Sets the fuel_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param fuel_type: The fuel_type of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._fuel_type = fuel_type

    @property
    def normal_capacity(self):
        """Gets the normal_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The normal_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: float
        """
        return self._normal_capacity

    @normal_capacity.setter
    def normal_capacity(self, normal_capacity):
        """Sets the normal_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param normal_capacity: The normal_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: float
        """

        self._normal_capacity = normal_capacity

    @property
    def available_capacity(self):
        """Gets the available_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The available_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: float
        """
        return self._available_capacity

    @available_capacity.setter
    def available_capacity(self, available_capacity):
        """Sets the available_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param available_capacity: The available_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: float
        """

        self._available_capacity = available_capacity

    @property
    def unavailable_capacity(self):
        """Gets the unavailable_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The unavailable_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: float
        """
        return self._unavailable_capacity

    @unavailable_capacity.setter
    def unavailable_capacity(self, unavailable_capacity):
        """Sets the unavailable_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param unavailable_capacity: The unavailable_capacity of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: float
        """

        self._unavailable_capacity = unavailable_capacity

    @property
    def event_status(self):
        """Gets the event_status of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The event_status of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param event_status: The event_status of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._event_status = event_status

    @property
    def event_start_time(self):
        """Gets the event_start_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The event_start_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: datetime
        """
        return self._event_start_time

    @event_start_time.setter
    def event_start_time(self, event_start_time):
        """Sets the event_start_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param event_start_time: The event_start_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: datetime
        """

        self._event_start_time = event_start_time

    @property
    def event_end_time(self):
        """Gets the event_end_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The event_end_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: datetime
        """
        return self._event_end_time

    @event_end_time.setter
    def event_end_time(self, event_end_time):
        """Sets the event_end_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param event_end_time: The event_end_time of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: datetime
        """

        self._event_end_time = event_end_time

    @property
    def duration_uncertainty(self):
        """Gets the duration_uncertainty of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The duration_uncertainty of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._duration_uncertainty

    @duration_uncertainty.setter
    def duration_uncertainty(self, duration_uncertainty):
        """Sets the duration_uncertainty of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param duration_uncertainty: The duration_uncertainty of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._duration_uncertainty = duration_uncertainty

    @property
    def cause(self):
        """Gets the cause of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The cause of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param cause: The cause of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._cause = cause

    @property
    def related_information(self):
        """Gets the related_information of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The related_information of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: str
        """
        return self._related_information

    @related_information.setter
    def related_information(self, related_information):
        """Sets the related_information of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param related_information: The related_information of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: str
        """

        self._related_information = related_information

    @property
    def outage_profile(self):
        """Gets the outage_profile of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The outage_profile of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: list[InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData]
        """
        return self._outage_profile

    @outage_profile.setter
    def outage_profile(self, outage_profile):
        """Sets the outage_profile of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param outage_profile: The outage_profile of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: list[InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData]
        """

        self._outage_profile = outage_profile

    @property
    def id(self):
        """Gets the id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501


        :return: The id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.


        :param id: The id of this InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
