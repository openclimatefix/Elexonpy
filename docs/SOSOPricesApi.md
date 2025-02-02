# swagger_client.SOSOPricesApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_soso_prices_from_from_to_to**](SOSOPricesApi.md#get_soso_prices_from_from_to_to) | **GET** /soso/prices | SO-SO prices (SOSO)

# **get_soso_prices_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSoSoPrices get_soso_prices_from_from_to_to(_from, to, format=format)

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
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # SO-SO prices (SOSO)
    api_response = api_instance.get_soso_prices_from_from_to_to(_from, to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SOSOPricesApi->get_soso_prices_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSoSoPrices**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSoSoPrices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

