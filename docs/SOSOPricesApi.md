# swagger_client.SOSOPricesApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**soso_prices_get**](SOSOPricesApi.md#soso_prices_get) | **GET** /soso/prices | SO-SO prices (SOSO)

# **soso_prices_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSoSoPrices soso_prices_get(_from, to, format=format)

SO-SO prices (SOSO)

This endpoint provides system operator to system operator prices data.  It can be filtered by start time.                This API endpoint has a maximum range of 24 hours.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SOSOPricesApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | 
to = '2013-10-20T19:20:30+01:00' # datetime | 
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # SO-SO prices (SOSO)
    api_response = api_instance.soso_prices_get(_from, to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SOSOPricesApi->soso_prices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSoSoPrices**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSoSoPrices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

