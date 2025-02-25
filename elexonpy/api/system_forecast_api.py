# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""



import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from elexonpy.api_client import ApiClient


class SystemForecastApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def forecast_system_loss_of_load_get(self, _from, to, **kwargs):  # noqa: E501
        """Loss of load probability and de-rated margin forecast (LOLPDRM)  # noqa: E501

        This endpoint provides the 1h, 2h, 4h, 8h and 12h+ Loss of Load Probability and De-rated Margin forecasts  for each settlement period over a requested time range.                For each forecast horizon at 1, 2, 4 or 8 hours, the returned value is the forecast received that number of hours  before the start of the settlement period.                For the forecast horizon of 12h, the returned value is the most recent forecast received 12 or more hours  before the start of the settlement period. That is, if the most recent forecast was published today at 00:00,  - for 11:30 today, the 12h forecast is the one published yesterday at 23:30 (12h before)  - for 12:00 today, the 12h forecast is the one published today at 00:00 (12h before)  - for 12:30 today, the 12h forecast is the one published today at 00:00 (the latest published)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forecast_system_loss_of_load_get(_from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _from: (required)
        :param datetime to: (required)
        :param int settlement_period_from: The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :param int settlement_period_to: The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.forecast_system_loss_of_load_get_with_http_info(_from, to, **kwargs)  # noqa: E501
        else:
            (data) = self.forecast_system_loss_of_load_get_with_http_info(_from, to, **kwargs)  # noqa: E501
            return data

    def forecast_system_loss_of_load_get_with_http_info(self, _from, to, **kwargs):  # noqa: E501
        """Loss of load probability and de-rated margin forecast (LOLPDRM)  # noqa: E501

        This endpoint provides the 1h, 2h, 4h, 8h and 12h+ Loss of Load Probability and De-rated Margin forecasts  for each settlement period over a requested time range.                For each forecast horizon at 1, 2, 4 or 8 hours, the returned value is the forecast received that number of hours  before the start of the settlement period.                For the forecast horizon of 12h, the returned value is the most recent forecast received 12 or more hours  before the start of the settlement period. That is, if the most recent forecast was published today at 00:00,  - for 11:30 today, the 12h forecast is the one published yesterday at 23:30 (12h before)  - for 12:00 today, the 12h forecast is the one published today at 00:00 (12h before)  - for 12:30 today, the 12h forecast is the one published today at 00:00 (the latest published)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forecast_system_loss_of_load_get_with_http_info(_from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _from: (required)
        :param datetime to: (required)
        :param int settlement_period_from: The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :param int settlement_period_to: The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_from', 'to', 'settlement_period_from', 'settlement_period_to', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method forecast_system_loss_of_load_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '_from' is set
        if ('_from' not in params or
                params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `forecast_system_loss_of_load_get`")  # noqa: E501
        # verify the required parameter 'to' is set
        if ('to' not in params or
                params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `forecast_system_loss_of_load_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'settlement_period_from' in params:
            query_params.append(('settlementPeriodFrom', params['settlement_period_from']))  # noqa: E501
        if 'settlement_period_to' in params:
            query_params.append(('settlementPeriodTo', params['settlement_period_to']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/forecast/system/loss-of-load', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
