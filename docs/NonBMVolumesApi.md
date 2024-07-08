# swagger_client.NonBMVolumesApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balancing_nonbm_volumes_get**](NonBMVolumesApi.md#balancing_nonbm_volumes_get) | **GET** /balancing/nonbm/volumes | Balancing services volume (QAS)

# **balancing_nonbm_volumes_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume balancing_nonbm_volumes_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, bm_unit=bm_unit, format=format)

Balancing services volume (QAS)

This endpoint provides balancing services volume data received from NGESO, with an added computed 'Time' field.  (The time field is calculated from the settlement date & period and represents the earliest possible time for  for which the datapoint applies)                Balancing services volume is a volume which is received from the System Operator, which represents the volume  of energy (MWh) associated with the provision of Applicable Balancing Services for each relevant BM Unit and  Settlement Period.    QAS can be positive or negative and is normally only provided where there is a non-zero volume.                By default, the from and to parameters filter the data by time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/nonbm/volumes?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/nonbm/volumes?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/nonbm/volumes?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/nonbm/volumes?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NonBMVolumesApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | The \"from\" start time or settlement date for the filter.
to = '2013-10-20T19:20:30+01:00' # datetime | The \"to\" start time or settlement date for the filter.
settlement_period_from = 56 # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
settlement_period_to = 56 # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
bm_unit = ['bm_unit_example'] # list[str] | The BM units to query. Add each unit separately. If no BM unit is selected all BM units will be displayed. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Balancing services volume (QAS)
    api_response = api_instance.balancing_nonbm_volumes_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NonBMVolumesApi->balancing_nonbm_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **bm_unit** | [**list[str]**](str.md)| The BM units to query. Add each unit separately. If no BM unit is selected all BM units will be displayed. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

