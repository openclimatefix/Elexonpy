# swagger_client.RollingSystemDemandApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generation_outturn_get**](RollingSystemDemandApi.md#generation_outturn_get) | **GET** /generation/outturn | Total generation outturn (FUELINST)

# **generation_outturn_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand generation_outturn_get(_from=_from, to=to, format=format)

Total generation outturn (FUELINST)

This endpoint provides the total generation outturn across all fuel types, derived by summing generation  of all categories from the Generation by Fuel Type report.                This data can be used as a proxy for rolling system demand.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.RollingSystemDemandApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime |  (optional)
to = '2013-10-20T19:20:30+01:00'  # datetime |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Total generation outturn (FUELINST)
    api_response = api_instance.generation_outturn_get(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RollingSystemDemandApi->generation_outturn_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

