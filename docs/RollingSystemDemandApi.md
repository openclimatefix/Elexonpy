# swagger_client.RollingSystemDemandApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_generation_outturn**](RollingSystemDemandApi.md#get_generation_outturn) | **GET** /generation/outturn | Total generation outturn (FUELINST)

# **get_generation_outturn**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand get_generation_outturn(_from=_from, to=to, format=format)

Total generation outturn (FUELINST)

This endpoint provides the total generation outturn across all fuel types, derived by summing generation  of all categories from the Generation by Fuel Type report.                This data can be used as a proxy for rolling system demand.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RollingSystemDemandApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Total generation outturn (FUELINST)
    api_response = api_instance.get_generation_outturn(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RollingSystemDemandApi->get_generation_outturn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

