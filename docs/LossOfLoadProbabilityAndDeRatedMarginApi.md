# swagger_client.LossOfLoadProbabilityAndDeRatedMarginApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lolpdrm_forecast_evolution**](LossOfLoadProbabilityAndDeRatedMarginApi.md#get_lolpdrm_forecast_evolution) | **GET** /lolpdrm/forecast/evolution | Loss of load probability and de-rated margin forecast (LOLPDRM)

# **get_lolpdrm_forecast_evolution**
> get_lolpdrm_forecast_evolution(format=format)

Loss of load probability and de-rated margin forecast (LOLPDRM)

This endpoint has been moved to forecast/system/loss-of-load.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LossOfLoadProbabilityAndDeRatedMarginApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Loss of load probability and de-rated margin forecast (LOLPDRM)
    api_instance.get_lolpdrm_forecast_evolution(format=format)
except ApiException as e:
    print("Exception when calling LossOfLoadProbabilityAndDeRatedMarginApi->get_lolpdrm_forecast_evolution: %s\n" % e)
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

