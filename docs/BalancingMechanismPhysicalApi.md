# swagger_client.BalancingMechanismPhysicalApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balancing_physical_all_dataset_dataset_settlementdate_settlementdate_set**](BalancingMechanismPhysicalApi.md#get_balancing_physical_all_dataset_dataset_settlementdate_settlementdate_set) | **GET** /balancing/physical/all | Market-wide physical data (PN, QPN, MILS, MELS)
[**get_balancing_physical_bmunit_bmunit_from_from_to_to**](BalancingMechanismPhysicalApi.md#get_balancing_physical_bmunit_bmunit_from_from_to_to) | **GET** /balancing/physical | Physical data per BMU (PN, QPN, MILS, MELS)

# **get_balancing_physical_all_dataset_dataset_settlementdate_settlementdate_set**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData get_balancing_physical_all_dataset_dataset_settlementdate_settlementdate_set(dataset, settlement_date, settlement_period, bm_unit=bm_unit, format=format)

Market-wide physical data (PN, QPN, MILS, MELS)

This endpoint provides the physical data for multiple requested BMUs or all BMUs.  It returns the data valid for a single settlement period.                Only one dataset can be queried at a time: PN, QPN, MILS, or MELS.  The results from each dataset are transformed to a common response model, with fields not present in all 4 datasets dropped.                The settlement period to query must be specified as a date and settlement period. The date must be given in the format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BalancingMechanismPhysicalApi()
dataset = 'dataset_example' # str | Dataset to query.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter.
settlement_period = 56 # int | Format - int32. The settlement period for the filter. This should be an integer from 1-50 inclusive.
bm_unit = ['bm_unit_example'] # list[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Market-wide physical data (PN, QPN, MILS, MELS)
    api_response = api_instance.get_balancing_physical_all_dataset_dataset_settlementdate_settlementdate_set(dataset, settlement_date, settlement_period, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancingMechanismPhysicalApi->get_balancing_physical_all_dataset_dataset_settlementdate_settlementdate_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Dataset to query. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. | 
 **settlement_period** | **int**| Format - int32. The settlement period for the filter. This should be an integer from 1-50 inclusive. | 
 **bm_unit** | [**list[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_physical_bmunit_bmunit_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData get_balancing_physical_bmunit_bmunit_from_from_to_to(bm_unit, _from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, dataset=dataset, format=format)

Physical data per BMU (PN, QPN, MILS, MELS)

This endpoint provides the physical data for a requested BMU.  It returns the data valid over a given time range.                By default, all of the relevant datasets are returned: PN, QPN, MILS, & MELS.  The results from each dataset are transformed to a common response model, with fields not present in all 4 datasets dropped.                By default, the from and to parameters filter the data by start time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of start time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/physical?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/physical?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/physical?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/physical?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BalancingMechanismPhysicalApi()
bm_unit = 'bm_unit_example' # str | The BM Unit to query.
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). The \"from\" start time or settlement date for the filter.
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). The \"to\" start time or settlement date for the filter.
settlement_period_from = 56 # int | Format - int32. The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
settlement_period_to = 56 # int | Format - int32. The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
dataset = ['dataset_example'] # list[str] | Datasets to filter. If empty, all datasets will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Physical data per BMU (PN, QPN, MILS, MELS)
    api_response = api_instance.get_balancing_physical_bmunit_bmunit_from_from_to_to(bm_unit, _from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, dataset=dataset, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancingMechanismPhysicalApi->get_balancing_physical_bmunit_bmunit_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_unit** | **str**| The BM Unit to query. | 
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| Format - int32. The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| Format - int32. The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **dataset** | [**list[str]**](str.md)| Datasets to filter. If empty, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

