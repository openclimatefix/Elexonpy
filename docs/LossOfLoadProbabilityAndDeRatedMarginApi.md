# swagger_client.LossOfLoadProbabilityAndDeRatedMarginApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lolpdrm_forecast_evolution_get**](LossOfLoadProbabilityAndDeRatedMarginApi.md#lolpdrm_forecast_evolution_get) | **GET** /lolpdrm/forecast/evolution | Loss of load probability and de-rated margin forecast (LOLPDRM)

# **lolpdrm_forecast_evolution_get**
> lolpdrm_forecast_evolution_get(format=format)

Loss of load probability and de-rated margin forecast (LOLPDRM)

This endpoint has been moved to forecast/system/loss-of-load.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.LossOfLoadProbabilityAndDeRatedMarginApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Loss of load probability and de-rated margin forecast (LOLPDRM)
    api_instance.lolpdrm_forecast_evolution_get(format=format)
except ApiException as e:
    print("Exception when calling LossOfLoadProbabilityAndDeRatedMarginApi->lolpdrm_forecast_evolution_get: %s\n" % e)
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

