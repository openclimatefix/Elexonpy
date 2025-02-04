# elexonpy.AvailabilityApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_generation_availability_summary14d**](AvailabilityApi.md#get_generation_availability_summary14d) | **GET** /generation/availability/summary/14D | [DEPRECATED] Fourteen-day generation forecast
[**get_generation_availability_summary3yw**](AvailabilityApi.md#get_generation_availability_summary3yw) | **GET** /generation/availability/summary/3YW | [DEPRECATED] Three-year generation forecast

# **get_generation_availability_summary14d**
> get_generation_availability_summary14d(format=format)

[DEPRECATED] Fourteen-day generation forecast

This endpoint has been moved to forecast/availability/daily.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.AvailabilityApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # [DEPRECATED] Fourteen-day generation forecast
    api_instance.get_generation_availability_summary14d(format=format)
except ApiException as e:
    print("Exception when calling AvailabilityApi->get_generation_availability_summary14d: %s\n" % e)
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

# **get_generation_availability_summary3yw**
> get_generation_availability_summary3yw(format=format)

[DEPRECATED] Three-year generation forecast

This endpoint has been moved to forecast/availability/weekly.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.AvailabilityApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # [DEPRECATED] Three-year generation forecast
    api_instance.get_generation_availability_summary3yw(format=format)
except ApiException as e:
    print("Exception when calling AvailabilityApi->get_generation_availability_summary3yw: %s\n" % e)
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

