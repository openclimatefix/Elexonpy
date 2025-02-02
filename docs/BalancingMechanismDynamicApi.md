# elexonpy.BalancingMechanismDynamicApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balancing_dynamic_all_settlementdate_settlementdate_settlementperiod_set**](BalancingMechanismDynamicApi.md#get_balancing_dynamic_all_settlementdate_settlementdate_settlementperiod_set) | **GET** /balancing/dynamic/all | Market-wide dynamic data (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)
[**get_balancing_dynamic_bmunit_bmunit_snapshotat_snapshotat**](BalancingMechanismDynamicApi.md#get_balancing_dynamic_bmunit_bmunit_snapshotat_snapshotat) | **GET** /balancing/dynamic | Dynamic data per BMU (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)
[**get_balancing_dynamic_rates_all_settlementdate_settlementdate_settlementperi**](BalancingMechanismDynamicApi.md#get_balancing_dynamic_rates_all_settlementdate_settlementdate_settlementperi) | **GET** /balancing/dynamic/rates/all | Market-wide rate data (RDRE, RURE, RDRI, RURI)
[**get_balancing_dynamic_rates_bmunit_bmunit_snapshotat_snapshotat**](BalancingMechanismDynamicApi.md#get_balancing_dynamic_rates_bmunit_bmunit_snapshotat_snapshotat) | **GET** /balancing/dynamic/rates | Rate data per BMU (RDRE, RURE, RDRI, RURI)

# **get_balancing_dynamic_all_settlementdate_settlementdate_settlementperiod_set**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData get_balancing_dynamic_all_settlementdate_settlementdate_settlementperiod_set(settlement_date, settlement_period, bm_unit=bm_unit, dataset=dataset, format=format)

Market-wide dynamic data (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)

This endpoint provides the dynamic data for multiple requested BMUs or all BMUs, excluding dynamic rate data.  It returns the data valid for a single settlement period. This includes a snapshot of data valid at the start  of the settlement period, and any changes published during that settlement period.                By default, all of the relevant datasets are returned: SIL, SEL, NDZ, NTB, NTO, MZT, MNZT, MDV & MDP.  The results from each dataset are transformed to a common response model, with the common integer field *Value*  mapped from the fields *Level*, *Period*, *Volume* or *Notice* in the original dataset, as relevant.                The settlement period must be specified as a date and settlement period. The date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BalancingMechanismDynamicApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date or datetime to filter.
settlement_period = 56 # int | Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive.
bm_unit = ['bm_unit_example'] # list[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
dataset = ['dataset_example'] # list[str] | Datasets to filter. If omitted, all datasets will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Market-wide dynamic data (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)
    api_response = api_instance.get_balancing_dynamic_all_settlementdate_settlementdate_settlementperiod_set(settlement_date, settlement_period, bm_unit=bm_unit, dataset=dataset, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancingMechanismDynamicApi->get_balancing_dynamic_all_settlementdate_settlementdate_settlementperiod_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date or datetime to filter. | 
 **settlement_period** | **int**| Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive. | 
 **bm_unit** | [**list[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **dataset** | [**list[str]**](str.md)| Datasets to filter. If omitted, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_dynamic_bmunit_bmunit_snapshotat_snapshotat**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData get_balancing_dynamic_bmunit_bmunit_snapshotat_snapshotat(bm_unit, snapshot_at, until=until, snapshot_at_settlement_period=snapshot_at_settlement_period, until_settlement_period=until_settlement_period, dataset=dataset, format=format)

Dynamic data per BMU (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)

This endpoint provides the dynamic data for a requested BMU, excluding physical rate data.  It returns a \"snapshot\" of data valid at a given time, and optionally a time series of changes over a requested interval.                By default, all of the relevant datasets are returned: SIL, SEL, NDZ, NTB, NTO, MZT, MNZT, MDV, MDP.  The results from each dataset are transformed to a common response model, with the common integer field *Value*  mapped from the fields *Level*, *Period*, *Volume* or *Notice* in the original dataset, as relevant.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BalancingMechanismDynamicApi()
bm_unit = 'bm_unit_example' # str | The BM Unit to query.
snapshot_at = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). When to retrieve a snapshot of data at.  That is, the latest datapoint before this time will be returned for each dataset.
until = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). When to retrieve data until.  Data from the snapshot until this time will be returned. (optional)
snapshot_at_settlement_period = 56 # int | Format - int32. The settlement period to retrieve a snapshot of data at.  If provided, the time part of SnapshotAt will be ignored. (optional)
until_settlement_period = 56 # int | Format - int32. The settlement period to retrieve data until.  If provided, the time part of Until will be ignored. (optional)
dataset = ['dataset_example'] # list[str] | Datasets to filter. If omitted, all datasets will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Dynamic data per BMU (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)
    api_response = api_instance.get_balancing_dynamic_bmunit_bmunit_snapshotat_snapshotat(bm_unit, snapshot_at, until=until, snapshot_at_settlement_period=snapshot_at_settlement_period, until_settlement_period=until_settlement_period, dataset=dataset, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancingMechanismDynamicApi->get_balancing_dynamic_bmunit_bmunit_snapshotat_snapshotat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_unit** | **str**| The BM Unit to query. | 
 **snapshot_at** | **datetime**| Format - date-time (as date-time in RFC3339). When to retrieve a snapshot of data at.  That is, the latest datapoint before this time will be returned for each dataset. | 
 **until** | **datetime**| Format - date-time (as date-time in RFC3339). When to retrieve data until.  Data from the snapshot until this time will be returned. | [optional] 
 **snapshot_at_settlement_period** | **int**| Format - int32. The settlement period to retrieve a snapshot of data at.  If provided, the time part of SnapshotAt will be ignored. | [optional] 
 **until_settlement_period** | **int**| Format - int32. The settlement period to retrieve data until.  If provided, the time part of Until will be ignored. | [optional] 
 **dataset** | [**list[str]**](str.md)| Datasets to filter. If omitted, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_dynamic_rates_all_settlementdate_settlementdate_settlementperi**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData get_balancing_dynamic_rates_all_settlementdate_settlementdate_settlementperi(settlement_date, settlement_period, bm_unit=bm_unit, dataset=dataset, format=format)

Market-wide rate data (RDRE, RURE, RDRI, RURI)

This endpoint provides market-wide physical rate data, for all BMUs or a requested set of multiple BMUs.  It returns the data valid for a given settlement period. This includes a snapshot of data valid at the start  of the settlement period, and any changes published during that settlement period.                The settlement period to query can be specified as a date and settlement period. The settlement date must be provided in the format yyyy-MM-dd.    By default, all of the relevant datasets are returned: RDRE, RURE, RDRI, RURI.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BalancingMechanismDynamicApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date to filter.
settlement_period = 56 # int | Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive.
bm_unit = ['bm_unit_example'] # list[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
dataset = ['dataset_example'] # list[str] | Datasets to return. If omitted, all datasets will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Market-wide rate data (RDRE, RURE, RDRI, RURI)
    api_response = api_instance.get_balancing_dynamic_rates_all_settlementdate_settlementdate_settlementperi(settlement_date, settlement_period, bm_unit=bm_unit, dataset=dataset, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancingMechanismDynamicApi->get_balancing_dynamic_rates_all_settlementdate_settlementdate_settlementperi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date to filter. | 
 **settlement_period** | **int**| Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive. | 
 **bm_unit** | [**list[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **dataset** | [**list[str]**](str.md)| Datasets to return. If omitted, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_dynamic_rates_bmunit_bmunit_snapshotat_snapshotat**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData get_balancing_dynamic_rates_bmunit_bmunit_snapshotat_snapshotat(bm_unit, snapshot_at, until=until, snapshot_at_settlement_period=snapshot_at_settlement_period, until_settlement_period=until_settlement_period, dataset=dataset, format=format)

Rate data per BMU (RDRE, RURE, RDRI, RURI)

This endpoint provides the physical rate data for a requested BMU.  It returns a \"snapshot\" of data valid at a given time, and optionally a time series of changes over a requested interval.                By default, all of the relevant datasets are returned: RDRE, RURE, RDRI, RURI.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BalancingMechanismDynamicApi()
bm_unit = 'bm_unit_example' # str | The BM Unit to query.
snapshot_at = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). When to retrieve a snapshot of data at.  That is, the latest datapoint before this time will be returned for each dataset.
until = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). When to retrieve data until.  Data from the snapshot until this time will be returned. (optional)
snapshot_at_settlement_period = 56 # int | Format - int32. The settlement period to retrieve a snapshot of data at.  If provided, the time part of SnapshotAt will be ignored. (optional)
until_settlement_period = 56 # int | Format - int32. The settlement period to retrieve data until.  If provided, the time part of Until will be ignored. (optional)
dataset = ['dataset_example'] # list[str] | Datasets to filter. If empty, all datasets will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Rate data per BMU (RDRE, RURE, RDRI, RURI)
    api_response = api_instance.get_balancing_dynamic_rates_bmunit_bmunit_snapshotat_snapshotat(bm_unit, snapshot_at, until=until, snapshot_at_settlement_period=snapshot_at_settlement_period, until_settlement_period=until_settlement_period, dataset=dataset, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancingMechanismDynamicApi->get_balancing_dynamic_rates_bmunit_bmunit_snapshotat_snapshotat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_unit** | **str**| The BM Unit to query. | 
 **snapshot_at** | **datetime**| Format - date-time (as date-time in RFC3339). When to retrieve a snapshot of data at.  That is, the latest datapoint before this time will be returned for each dataset. | 
 **until** | **datetime**| Format - date-time (as date-time in RFC3339). When to retrieve data until.  Data from the snapshot until this time will be returned. | [optional] 
 **snapshot_at_settlement_period** | **int**| Format - int32. The settlement period to retrieve a snapshot of data at.  If provided, the time part of SnapshotAt will be ignored. | [optional] 
 **until_settlement_period** | **int**| Format - int32. The settlement period to retrieve data until.  If provided, the time part of Until will be ignored. | [optional] 
 **dataset** | [**list[str]**](str.md)| Datasets to filter. If empty, all datasets will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

