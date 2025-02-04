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

class InsightsApiLegacyInteroperabilityLegacyRemitListItem(object):
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
        'message_id': 'str',
        'sequence_id': 'int',
        'message_heading': 'str',
        'event_type': 'str',
        'publish_date_time_string': 'str',
        'participant_market_participant_id': 'str',
        'asset_id': 'str',
        'asset_eic_code': 'str',
        'asset_type': 'str',
        'affected_unit': 'str',
        'affected_area': 'str',
        'asset_fuel_type': 'str',
        'asset_normal_capacity': 'float',
        'asset_normal_capacity_specified': 'bool',
        'available_capacity': 'float',
        'available_capacity_specified': 'bool',
        'event_start_string': 'str',
        'event_end_string': 'str',
        'duration_uncertainty': 'str',
        'cause': 'str',
        'event_status': 'str',
        'related_information': 'str',
        'active_flag': 'str',
        'revision_number': 'int',
        'message_type': 'str',
        'unavailability_type': 'str',
        'unavailable_capacity': 'float',
        'unavailable_capacity_specified': 'bool'
    }

    attribute_map = {
        'message_id': 'messageId',
        'sequence_id': 'sequenceId',
        'message_heading': 'messageHeading',
        'event_type': 'eventType',
        'publish_date_time_string': 'publishDateTimeString',
        'participant_market_participant_id': 'participantMarketParticipantId',
        'asset_id': 'assetId',
        'asset_eic_code': 'assetEicCode',
        'asset_type': 'assetType',
        'affected_unit': 'affectedUnit',
        'affected_area': 'affectedArea',
        'asset_fuel_type': 'assetFuelType',
        'asset_normal_capacity': 'assetNormalCapacity',
        'asset_normal_capacity_specified': 'assetNormalCapacitySpecified',
        'available_capacity': 'availableCapacity',
        'available_capacity_specified': 'availableCapacitySpecified',
        'event_start_string': 'eventStartString',
        'event_end_string': 'eventEndString',
        'duration_uncertainty': 'durationUncertainty',
        'cause': 'cause',
        'event_status': 'eventStatus',
        'related_information': 'relatedInformation',
        'active_flag': 'activeFlag',
        'revision_number': 'revisionNumber',
        'message_type': 'messageType',
        'unavailability_type': 'unavailabilityType',
        'unavailable_capacity': 'unavailableCapacity',
        'unavailable_capacity_specified': 'unavailableCapacitySpecified'
    }

    def __init__(self, message_id=None, sequence_id=None, message_heading=None, event_type=None, publish_date_time_string=None, participant_market_participant_id=None, asset_id=None, asset_eic_code=None, asset_type=None, affected_unit=None, affected_area=None, asset_fuel_type=None, asset_normal_capacity=None, asset_normal_capacity_specified=None, available_capacity=None, available_capacity_specified=None, event_start_string=None, event_end_string=None, duration_uncertainty=None, cause=None, event_status=None, related_information=None, active_flag=None, revision_number=None, message_type=None, unavailability_type=None, unavailable_capacity=None, unavailable_capacity_specified=None):  # noqa: E501
        """InsightsApiLegacyInteroperabilityLegacyRemitListItem - a model defined in Swagger"""  # noqa: E501
        self._message_id = None
        self._sequence_id = None
        self._message_heading = None
        self._event_type = None
        self._publish_date_time_string = None
        self._participant_market_participant_id = None
        self._asset_id = None
        self._asset_eic_code = None
        self._asset_type = None
        self._affected_unit = None
        self._affected_area = None
        self._asset_fuel_type = None
        self._asset_normal_capacity = None
        self._asset_normal_capacity_specified = None
        self._available_capacity = None
        self._available_capacity_specified = None
        self._event_start_string = None
        self._event_end_string = None
        self._duration_uncertainty = None
        self._cause = None
        self._event_status = None
        self._related_information = None
        self._active_flag = None
        self._revision_number = None
        self._message_type = None
        self._unavailability_type = None
        self._unavailable_capacity = None
        self._unavailable_capacity_specified = None
        self.discriminator = None
        if message_id is not None:
            self.message_id = message_id
        if sequence_id is not None:
            self.sequence_id = sequence_id
        if message_heading is not None:
            self.message_heading = message_heading
        if event_type is not None:
            self.event_type = event_type
        if publish_date_time_string is not None:
            self.publish_date_time_string = publish_date_time_string
        if participant_market_participant_id is not None:
            self.participant_market_participant_id = participant_market_participant_id
        if asset_id is not None:
            self.asset_id = asset_id
        if asset_eic_code is not None:
            self.asset_eic_code = asset_eic_code
        if asset_type is not None:
            self.asset_type = asset_type
        if affected_unit is not None:
            self.affected_unit = affected_unit
        if affected_area is not None:
            self.affected_area = affected_area
        if asset_fuel_type is not None:
            self.asset_fuel_type = asset_fuel_type
        if asset_normal_capacity is not None:
            self.asset_normal_capacity = asset_normal_capacity
        if asset_normal_capacity_specified is not None:
            self.asset_normal_capacity_specified = asset_normal_capacity_specified
        if available_capacity is not None:
            self.available_capacity = available_capacity
        if available_capacity_specified is not None:
            self.available_capacity_specified = available_capacity_specified
        if event_start_string is not None:
            self.event_start_string = event_start_string
        if event_end_string is not None:
            self.event_end_string = event_end_string
        if duration_uncertainty is not None:
            self.duration_uncertainty = duration_uncertainty
        if cause is not None:
            self.cause = cause
        if event_status is not None:
            self.event_status = event_status
        if related_information is not None:
            self.related_information = related_information
        if active_flag is not None:
            self.active_flag = active_flag
        if revision_number is not None:
            self.revision_number = revision_number
        if message_type is not None:
            self.message_type = message_type
        if unavailability_type is not None:
            self.unavailability_type = unavailability_type
        if unavailable_capacity is not None:
            self.unavailable_capacity = unavailable_capacity
        if unavailable_capacity_specified is not None:
            self.unavailable_capacity_specified = unavailable_capacity_specified

    @property
    def message_id(self):
        """Gets the message_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The message_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param message_id: The message_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def sequence_id(self):
        """Gets the sequence_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The sequence_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: int
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """Sets the sequence_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param sequence_id: The sequence_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: int
        """

        self._sequence_id = sequence_id

    @property
    def message_heading(self):
        """Gets the message_heading of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The message_heading of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._message_heading

    @message_heading.setter
    def message_heading(self, message_heading):
        """Sets the message_heading of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param message_heading: The message_heading of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._message_heading = message_heading

    @property
    def event_type(self):
        """Gets the event_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The event_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param event_type: The event_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def publish_date_time_string(self):
        """Gets the publish_date_time_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The publish_date_time_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._publish_date_time_string

    @publish_date_time_string.setter
    def publish_date_time_string(self, publish_date_time_string):
        """Sets the publish_date_time_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param publish_date_time_string: The publish_date_time_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._publish_date_time_string = publish_date_time_string

    @property
    def participant_market_participant_id(self):
        """Gets the participant_market_participant_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The participant_market_participant_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._participant_market_participant_id

    @participant_market_participant_id.setter
    def participant_market_participant_id(self, participant_market_participant_id):
        """Sets the participant_market_participant_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param participant_market_participant_id: The participant_market_participant_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._participant_market_participant_id = participant_market_participant_id

    @property
    def asset_id(self):
        """Gets the asset_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The asset_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param asset_id: The asset_id of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def asset_eic_code(self):
        """Gets the asset_eic_code of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The asset_eic_code of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._asset_eic_code

    @asset_eic_code.setter
    def asset_eic_code(self, asset_eic_code):
        """Sets the asset_eic_code of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param asset_eic_code: The asset_eic_code of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._asset_eic_code = asset_eic_code

    @property
    def asset_type(self):
        """Gets the asset_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The asset_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param asset_type: The asset_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._asset_type = asset_type

    @property
    def affected_unit(self):
        """Gets the affected_unit of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The affected_unit of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._affected_unit

    @affected_unit.setter
    def affected_unit(self, affected_unit):
        """Sets the affected_unit of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param affected_unit: The affected_unit of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._affected_unit = affected_unit

    @property
    def affected_area(self):
        """Gets the affected_area of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The affected_area of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._affected_area

    @affected_area.setter
    def affected_area(self, affected_area):
        """Sets the affected_area of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param affected_area: The affected_area of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._affected_area = affected_area

    @property
    def asset_fuel_type(self):
        """Gets the asset_fuel_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The asset_fuel_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._asset_fuel_type

    @asset_fuel_type.setter
    def asset_fuel_type(self, asset_fuel_type):
        """Sets the asset_fuel_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param asset_fuel_type: The asset_fuel_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._asset_fuel_type = asset_fuel_type

    @property
    def asset_normal_capacity(self):
        """Gets the asset_normal_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The asset_normal_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: float
        """
        return self._asset_normal_capacity

    @asset_normal_capacity.setter
    def asset_normal_capacity(self, asset_normal_capacity):
        """Sets the asset_normal_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param asset_normal_capacity: The asset_normal_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: float
        """

        self._asset_normal_capacity = asset_normal_capacity

    @property
    def asset_normal_capacity_specified(self):
        """Gets the asset_normal_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The asset_normal_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: bool
        """
        return self._asset_normal_capacity_specified

    @asset_normal_capacity_specified.setter
    def asset_normal_capacity_specified(self, asset_normal_capacity_specified):
        """Sets the asset_normal_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param asset_normal_capacity_specified: The asset_normal_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: bool
        """

        self._asset_normal_capacity_specified = asset_normal_capacity_specified

    @property
    def available_capacity(self):
        """Gets the available_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The available_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: float
        """
        return self._available_capacity

    @available_capacity.setter
    def available_capacity(self, available_capacity):
        """Sets the available_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param available_capacity: The available_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: float
        """

        self._available_capacity = available_capacity

    @property
    def available_capacity_specified(self):
        """Gets the available_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The available_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: bool
        """
        return self._available_capacity_specified

    @available_capacity_specified.setter
    def available_capacity_specified(self, available_capacity_specified):
        """Sets the available_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param available_capacity_specified: The available_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: bool
        """

        self._available_capacity_specified = available_capacity_specified

    @property
    def event_start_string(self):
        """Gets the event_start_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The event_start_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._event_start_string

    @event_start_string.setter
    def event_start_string(self, event_start_string):
        """Sets the event_start_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param event_start_string: The event_start_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._event_start_string = event_start_string

    @property
    def event_end_string(self):
        """Gets the event_end_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The event_end_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._event_end_string

    @event_end_string.setter
    def event_end_string(self, event_end_string):
        """Sets the event_end_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param event_end_string: The event_end_string of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._event_end_string = event_end_string

    @property
    def duration_uncertainty(self):
        """Gets the duration_uncertainty of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The duration_uncertainty of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._duration_uncertainty

    @duration_uncertainty.setter
    def duration_uncertainty(self, duration_uncertainty):
        """Sets the duration_uncertainty of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param duration_uncertainty: The duration_uncertainty of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._duration_uncertainty = duration_uncertainty

    @property
    def cause(self):
        """Gets the cause of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The cause of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param cause: The cause of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._cause = cause

    @property
    def event_status(self):
        """Gets the event_status of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The event_status of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param event_status: The event_status of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._event_status = event_status

    @property
    def related_information(self):
        """Gets the related_information of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The related_information of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._related_information

    @related_information.setter
    def related_information(self, related_information):
        """Sets the related_information of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param related_information: The related_information of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._related_information = related_information

    @property
    def active_flag(self):
        """Gets the active_flag of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The active_flag of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._active_flag

    @active_flag.setter
    def active_flag(self, active_flag):
        """Sets the active_flag of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param active_flag: The active_flag of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._active_flag = active_flag

    @property
    def revision_number(self):
        """Gets the revision_number of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The revision_number of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: int
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param revision_number: The revision_number of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: int
        """

        self._revision_number = revision_number

    @property
    def message_type(self):
        """Gets the message_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The message_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param message_type: The message_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._message_type = message_type

    @property
    def unavailability_type(self):
        """Gets the unavailability_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The unavailability_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: str
        """
        return self._unavailability_type

    @unavailability_type.setter
    def unavailability_type(self, unavailability_type):
        """Sets the unavailability_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param unavailability_type: The unavailability_type of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: str
        """

        self._unavailability_type = unavailability_type

    @property
    def unavailable_capacity(self):
        """Gets the unavailable_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The unavailable_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: float
        """
        return self._unavailable_capacity

    @unavailable_capacity.setter
    def unavailable_capacity(self, unavailable_capacity):
        """Sets the unavailable_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param unavailable_capacity: The unavailable_capacity of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: float
        """

        self._unavailable_capacity = unavailable_capacity

    @property
    def unavailable_capacity_specified(self):
        """Gets the unavailable_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501


        :return: The unavailable_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :rtype: bool
        """
        return self._unavailable_capacity_specified

    @unavailable_capacity_specified.setter
    def unavailable_capacity_specified(self, unavailable_capacity_specified):
        """Sets the unavailable_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.


        :param unavailable_capacity_specified: The unavailable_capacity_specified of this InsightsApiLegacyInteroperabilityLegacyRemitListItem.  # noqa: E501
        :type: bool
        """

        self._unavailable_capacity_specified = unavailable_capacity_specified

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
        if issubclass(InsightsApiLegacyInteroperabilityLegacyRemitListItem, dict):
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
        if not isinstance(other, InsightsApiLegacyInteroperabilityLegacyRemitListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
