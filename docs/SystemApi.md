# elexonpy.SystemApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_demand_control_instructions**](SystemApi.md#get_system_demand_control_instructions) | **GET** /system/demand-control-instructions | Demand control instructions (DCI)
[**get_system_frequency**](SystemApi.md#get_system_frequency) | **GET** /system/frequency | System frequency (FREQ)
[**get_system_frequency_stream**](SystemApi.md#get_system_frequency_stream) | **GET** /system/frequency/stream | System frequency (FREQ) stream
[**get_system_warnings**](SystemApi.md#get_system_warnings) | **GET** /system/warnings | System warnings (SYSWARN)

# **get_system_demand_control_instructions**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData get_system_demand_control_instructions(_from=_from, to=to, format=format)

Demand control instructions (DCI)

This endpoint provides demand control instruction data, filtered by the time range of the instruction.  There is no date range limit on parameters.  If no query parameters are supplied all data is returned.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.SystemApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Demand control instructions (DCI)
    api_response = api_instance.get_system_demand_control_instructions(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_demand_control_instructions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_frequency**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency get_system_frequency(_from=_from, to=to, format=format)

System frequency (FREQ)

This endpoint allows for retrieving a collection of recent system frequency data from National Grid ESO. Results  can be filtered by a range of DateTime parameters. This endpoint is useful for ad-hoc querying frequency data.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.SystemApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # System frequency (FREQ)
    api_response = api_instance.get_system_frequency(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_frequency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_frequency_stream**
> list[InsightsApiModelsResponsesMiscSystemFrequency] get_system_frequency_stream(_from=_from, to=to)

System frequency (FREQ) stream

This endpoint allows for retrieving a stream of recent system frequency data from National Grid ESO. Results can  be filtered by a range of DateTime parameters. This endpoint has an optimised JSON payload and aimed at frequent  request for the frequency data.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.SystemApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)

try:
    # System frequency (FREQ) stream
    api_response = api_instance.get_system_frequency_stream(_from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_frequency_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 

### Return type

[**list[InsightsApiModelsResponsesMiscSystemFrequency]**](InsightsApiModelsResponsesMiscSystemFrequency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_warnings**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData get_system_warnings(warning_type=warning_type, publish_date_time_from=publish_date_time_from, publish_date_time_to=publish_date_time_to, format=format)

System warnings (SYSWARN)

This endpoint provides system warnings data. Results can be filtered by warning type and a range of DateTime parameters.  - If no parameters are specified then the latest message is returned  - If just a warning type is specified then the latest message of that type is returned  - If just publish times are specified then all messages within that range are returned

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.SystemApi()
warning_type = 'warning_type_example' # str |  (optional)
publish_date_time_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
publish_date_time_to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # System warnings (SYSWARN)
    api_response = api_instance.get_system_warnings(warning_type=warning_type, publish_date_time_from=publish_date_time_from, publish_date_time_to=publish_date_time_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_warnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warning_type** | **str**|  | [optional] 
 **publish_date_time_from** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **publish_date_time_to** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

