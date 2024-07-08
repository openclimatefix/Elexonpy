# swagger_client.TemperatureApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temperature_get**](TemperatureApi.md#temperature_get) | **GET** /temperature | Temperature data (TEMP)

# **temperature_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData temperature_get(_from=_from, to=to, format=format)

Temperature data (TEMP)

This endpoint provides daily average GB temperature data (in Celsius) as well as reference temperatures (low, normal and high).  This average data is calculated by National Grid ESO from the data retrieved from 6 weather stations around Britain.  NGESO use this data as part of the electricity demand forecasting process.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemperatureApi()
_from = '2013-10-20' # date | The from date for the filter. This must be in the format yyyy-MM-dd. (optional)
to = '2013-10-20' # date | The to date for the filter. This must be in the format yyyy-MM-dd. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Temperature data (TEMP)
    api_response = api_instance.temperature_get(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemperatureApi->temperature_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| The from date for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **to** | **date**| The to date for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

