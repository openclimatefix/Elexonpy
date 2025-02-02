# swagger_client.TemperatureApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_temperature**](TemperatureApi.md#get_temperature) | **GET** /temperature | Temperature data (TEMP)

# **get_temperature**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData get_temperature(_from=_from, to=to, format=format)

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
_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). The from date for the filter. This must be in the format yyyy-MM-dd. (optional)
to = '2013-10-20' # date | Format - date (as full-date in RFC3339). The to date for the filter. This must be in the format yyyy-MM-dd. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Temperature data (TEMP)
    api_response = api_instance.get_temperature(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemperatureApi->get_temperature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Format - date (as full-date in RFC3339). The from date for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **to** | **date**| Format - date (as full-date in RFC3339). The to date for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

