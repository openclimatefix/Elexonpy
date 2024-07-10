# swagger_client.AvailabilityApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generation_availability_summary14_d_get**](AvailabilityApi.md#generation_availability_summary14_d_get) | **GET** /generation/availability/summary/14D | Fourteen-day generation forecast
[**generation_availability_summary3_yw_get**](AvailabilityApi.md#generation_availability_summary3_yw_get) | **GET** /generation/availability/summary/3YW | Three-year generation forecast

# **generation_availability_summary14_d_get**
> generation_availability_summary14_d_get(format=format)

Fourteen-day generation forecast

This endpoint has been moved to forecast/availability/summary/14D.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.AvailabilityApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Fourteen-day generation forecast
    api_instance.generation_availability_summary14_d_get(format=format)
except ApiException as e:
    print("Exception when calling AvailabilityApi->generation_availability_summary14_d_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generation_availability_summary3_yw_get**
> generation_availability_summary3_yw_get(format=format)

Three-year generation forecast

This endpoint has been moved to forecast/availability/summary/3YW.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.AvailabilityApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Three-year generation forecast
    api_instance.generation_availability_summary3_yw_get(format=format)
except ApiException as e:
    print("Exception when calling AvailabilityApi->generation_availability_summary3_yw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

