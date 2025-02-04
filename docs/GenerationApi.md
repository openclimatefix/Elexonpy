# elexonpy.GenerationApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_generation_actual_per_type_day_total**](GenerationApi.md#get_generation_actual_per_type_day_total) | **GET** /generation/actual/per-type/day-total | Current snapshot of actual generation by fuel type categories (AGPT/B1620)
[**get_generation_actual_per_type_from_from_to_to**](GenerationApi.md#get_generation_actual_per_type_from_from_to_to) | **GET** /generation/actual/per-type | Historic actual generation automatically down-sampled (AGPT/B1620)
[**get_generation_actual_per_type_wind_and_solar_from_from_to_to**](GenerationApi.md#get_generation_actual_per_type_wind_and_solar_from_from_to_to) | **GET** /generation/actual/per-type/wind-and-solar | Historic actual or estimated wind and solar power generation (AGWS/B1630)
[**get_generation_outturn**](GenerationApi.md#get_generation_outturn) | **GET** /generation/outturn | Total generation outturn (FUELINST)
[**get_generation_outturn_current**](GenerationApi.md#get_generation_outturn_current) | **GET** /generation/outturn/current | Current snapshot of generation by fuel type categories (FUELINST, FUELHH)
[**get_generation_outturn_fuelinsthhcur**](GenerationApi.md#get_generation_outturn_fuelinsthhcur) | **GET** /generation/outturn/FUELINSTHHCUR | This endpoint is obsolete, and this location may be removed with no further notice. 
[**get_generation_outturn_halfhourlyinterconnector**](GenerationApi.md#get_generation_outturn_halfhourlyinterconnector) | **GET** /generation/outturn/halfHourlyInterconnector | This endpoint is obsolete, and this location may be removed with no further notice. 
[**get_generation_outturn_interconnectors**](GenerationApi.md#get_generation_outturn_interconnectors) | **GET** /generation/outturn/interconnectors | Historic half-hourly interconnector flows (FUELINST)
[**get_generation_outturn_summary**](GenerationApi.md#get_generation_outturn_summary) | **GET** /generation/outturn/summary | Historic generation automatically down-sampled (FUELINST)

# **get_generation_actual_per_type_day_total**
> list[InsightsApiModelsResponsesTransparencyAgptSummaryData] get_generation_actual_per_type_day_total(format=format)

Current snapshot of actual generation by fuel type categories (AGPT/B1620)

This endpoint provides aggregated AGPT (B1620) data. It returns totals and percentages  for the last half hour and 24 hours for each generation type.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Current snapshot of actual generation by fuel type categories (AGPT/B1620)
    api_response = api_instance.get_generation_actual_per_type_day_total(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_actual_per_type_day_total: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**list[InsightsApiModelsResponsesTransparencyAgptSummaryData]**](InsightsApiModelsResponsesTransparencyAgptSummaryData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generation_actual_per_type_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod get_generation_actual_per_type_from_from_to_to(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Historic actual generation automatically down-sampled (AGPT/B1620)

⚠ This endpoint provides a down-sampled data summary intended for visualisation purposes.  Depending on the quantity of data requested, data returned may be averaged hourly, daily,  weekly or monthly. Quantities are rounded to the nearest MWh.  Use /datasets/AGPT for full access.                This endpoint provides actual aggregated generation data per Power System Resource type   (Fuel Type categories as defined by Commission Regulation (EU) No 543/2013).    This endpoint filters by startTime, and groups results by settlement period.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
settlement_period_from = 56 # int | Format - int32. (optional)
settlement_period_to = 56 # int | Format - int32. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic actual generation automatically down-sampled (AGPT/B1620)
    api_response = api_instance.get_generation_actual_per_type_from_from_to_to(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_actual_per_type_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **settlement_period_from** | **int**| Format - int32. | [optional] 
 **settlement_period_to** | **int**| Format - int32. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generation_actual_per_type_wind_and_solar_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar get_generation_actual_per_type_wind_and_solar_from_from_to_to(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Historic actual or estimated wind and solar power generation (AGWS/B1630)

This endpoint provides actual or estimated wind and solar power generation  per settlement period. It returns generation with Power System Resource type  Solar, Wind Onshore or Wind Offshore (Fuel Type categories as defined by  Commission Regulation (EU) No 543/2013).                This endpoint filters by startTime and provides a maximum data output range of 7 days.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
settlement_period_from = 56 # int | Format - int32. (optional)
settlement_period_to = 56 # int | Format - int32. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic actual or estimated wind and solar power generation (AGWS/B1630)
    api_response = api_instance.get_generation_actual_per_type_wind_and_solar_from_from_to_to(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_actual_per_type_wind_and_solar_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **settlement_period_from** | **int**| Format - int32. | [optional] 
 **settlement_period_to** | **int**| Format - int32. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generation_outturn**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand get_generation_outturn(_from=_from, to=to, format=format)

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
api_instance = elexonpy.GenerationApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Total generation outturn (FUELINST)
    api_response = api_instance.get_generation_outturn(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_outturn: %s\n" % e)
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

# **get_generation_outturn_current**
> list[InsightsApiModelsResponsesGenerationGenerationByFuelType] get_generation_outturn_current(fuel_type=fuel_type, format=format)

Current snapshot of generation by fuel type categories (FUELINST, FUELHH)

This endpoint provides a snapshot view of the last 24 hours generation by individual fuel type categories including interconnector.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationApi()
fuel_type = ['fuel_type_example'] # list[str] |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Current snapshot of generation by fuel type categories (FUELINST, FUELHH)
    api_response = api_instance.get_generation_outturn_current(fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_outturn_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**list[InsightsApiModelsResponsesGenerationGenerationByFuelType]**](InsightsApiModelsResponsesGenerationGenerationByFuelType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generation_outturn_fuelinsthhcur**
> get_generation_outturn_fuelinsthhcur(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to generation/outturn/current.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.get_generation_outturn_fuelinsthhcur(format=format)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_outturn_fuelinsthhcur: %s\n" % e)
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

# **get_generation_outturn_halfhourlyinterconnector**
> get_generation_outturn_halfhourlyinterconnector(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to generation/outturn/interconnectors.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.get_generation_outturn_halfhourlyinterconnector(format=format)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_outturn_halfhourlyinterconnector: %s\n" % e)
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

# **get_generation_outturn_interconnectors**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn get_generation_outturn_interconnectors(publish_date_time_from=publish_date_time_from, publish_date_time_to=publish_date_time_to, settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, interconnector_name=interconnector_name, format=format)

Historic half-hourly interconnector flows (FUELINST)

This endpoint provides the interconnector flows report derived from the Generation by Fuel Type (FUELINST)  data and shows both interconnector imports and exports; the data is updated every five minutes.                Settlement date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationApi()
publish_date_time_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
publish_date_time_to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
settlement_date_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date from filter. This must be in the format yyyy-MM-dd. (optional)
settlement_date_to = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd. (optional)
settlement_period = [56] # list[int] |  (optional)
interconnector_name = ['interconnector_name_example'] # list[str] |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic half-hourly interconnector flows (FUELINST)
    api_response = api_instance.get_generation_outturn_interconnectors(publish_date_time_from=publish_date_time_from, publish_date_time_to=publish_date_time_to, settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, interconnector_name=interconnector_name, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_outturn_interconnectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_date_time_from** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **publish_date_time_to** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **settlement_date_from** | **date**| Format - date (as full-date in RFC3339). The settlement date from filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_date_to** | **date**| Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_period** | [**list[int]**](int.md)|  | [optional] 
 **interconnector_name** | [**list[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generation_outturn_summary**
> list[InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod] get_generation_outturn_summary(start_time=start_time, end_time=end_time, include_negative_generation=include_negative_generation, format=format)

Historic generation automatically down-sampled (FUELINST)

⚠ This endpoint provides a down-sampled data summary intended for visualisation purposes.  Use raw dataset endpoints under /datasets for full access.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
include_negative_generation = true # bool |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic generation automatically down-sampled (FUELINST)
    api_response = api_instance.get_generation_outturn_summary(start_time=start_time, end_time=end_time, include_negative_generation=include_negative_generation, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationApi->get_generation_outturn_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **end_time** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **include_negative_generation** | **bool**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**list[InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod]**](InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

