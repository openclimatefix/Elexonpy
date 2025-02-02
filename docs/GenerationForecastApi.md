# swagger_client.GenerationForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forecast_availability_daily**](GenerationForecastApi.md#get_forecast_availability_daily) | **GET** /forecast/availability/daily | Fourteen-day generation capacity forecast (FOU2T14D)
[**get_forecast_availability_daily_evolution_forecastdate_forecastdate**](GenerationForecastApi.md#get_forecast_availability_daily_evolution_forecastdate_forecastdate) | **GET** /forecast/availability/daily/evolution | Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)
[**get_forecast_availability_daily_history_publishtime_publishtime**](GenerationForecastApi.md#get_forecast_availability_daily_history_publishtime_publishtime) | **GET** /forecast/availability/daily/history | History of the fourteen-day generation capacity forecast (FOU2T14D)
[**get_forecast_availability_summary14d**](GenerationForecastApi.md#get_forecast_availability_summary14d) | **GET** /forecast/availability/summary/14D | This endpoint is obsolete, and this location may be removed with no further notice. Use forecast/availability/daily instead
[**get_forecast_availability_summary3yw**](GenerationForecastApi.md#get_forecast_availability_summary3yw) | **GET** /forecast/availability/summary/3YW | This endpoint is obsolete, and this location may be removed with no further notice. Use forecast/availability/weekly instead
[**get_forecast_availability_weekly**](GenerationForecastApi.md#get_forecast_availability_weekly) | **GET** /forecast/availability/weekly | Three-year generation capacity forecast (FOU2T3YW)
[**get_forecast_availability_weekly_evolution_year_year_week_week**](GenerationForecastApi.md#get_forecast_availability_weekly_evolution_year_year_week_week) | **GET** /forecast/availability/weekly/evolution | Evolution of the three-year generation capacity forecast over time (FOU2T3YW)
[**get_forecast_availability_weekly_history_publishtime_publishtime**](GenerationForecastApi.md#get_forecast_availability_weekly_history_publishtime_publishtime) | **GET** /forecast/availability/weekly/history | History of the three-year generation capacity forecast (FOU2T3YW)
[**get_forecast_generation_day_ahead_from_from_to_to**](GenerationForecastApi.md#get_forecast_generation_day_ahead_from_from_to_to) | **GET** /forecast/generation/day-ahead | Day-ahead aggregated generation (DAG/B1430)
[**get_forecast_generation_wind**](GenerationForecastApi.md#get_forecast_generation_wind) | **GET** /forecast/generation/wind | Current wind generation forecast (WINDFOR)
[**get_forecast_generation_wind_and_solar_day_ahead_from_from_to_to_processtype**](GenerationForecastApi.md#get_forecast_generation_wind_and_solar_day_ahead_from_from_to_to_processtype) | **GET** /forecast/generation/wind-and-solar/day-ahead | Day-ahead generation forecast for wind and solar (DGWS/B1440)
[**get_forecast_generation_wind_earliest_from_from_to_to**](GenerationForecastApi.md#get_forecast_generation_wind_earliest_from_from_to_to) | **GET** /forecast/generation/wind/earliest | Historic view of the earliest forecasted wind generation (WINDFOR)
[**get_forecast_generation_wind_earliest_stream_from_from_to_to**](GenerationForecastApi.md#get_forecast_generation_wind_earliest_stream_from_from_to_to) | **GET** /forecast/generation/wind/earliest/stream | Historic view of the earliest forecasted wind generation (WINDFOR) stream
[**get_forecast_generation_wind_evolution_starttime_starttime**](GenerationForecastApi.md#get_forecast_generation_wind_evolution_starttime_starttime) | **GET** /forecast/generation/wind/evolution | Evolution of the wind generation forecast over time (WINDFOR)
[**get_forecast_generation_wind_history_publishtime_publishtime**](GenerationForecastApi.md#get_forecast_generation_wind_history_publishtime_publishtime) | **GET** /forecast/generation/wind/history | History of the wind generation forecast (WINDFOR)
[**get_forecast_generation_wind_latest_from_from_to_to**](GenerationForecastApi.md#get_forecast_generation_wind_latest_from_from_to_to) | **GET** /forecast/generation/wind/latest | Historic view of the latest forecasted wind generation (WINDFOR)
[**get_forecast_generation_wind_latest_stream_from_from_to_to**](GenerationForecastApi.md#get_forecast_generation_wind_latest_stream_from_from_to_to) | **GET** /forecast/generation/wind/latest/stream | Historic view of the latest forecasted wind generation (WINDFOR) stream
[**get_forecast_generation_wind_peak**](GenerationForecastApi.md#get_forecast_generation_wind_peak) | **GET** /forecast/generation/wind/peak | Peak wind generation forecast for each day (WINDFOR)

# **get_forecast_availability_daily**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily get_forecast_availability_daily(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Fourteen-day generation capacity forecast (FOU2T14D)

This endpoint provides the latest fourteen-day generation forecast

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
level = 'level_example' # str | The filter level for the forecast. This can be one of the following:  - `total`: the total forecast for the given time period.  - `bmUnit`: the forecast for each specified BM unit.  - `fuelType`: the forecast aggregated, and optionally filtered by fuel type. (optional)
bm_unit = ['bm_unit_example'] # list[str] | The BM units to query. Add each unit separately. Either the Elexon ID (Eg: `T_CARR-1`) or National Grid ID (Eg: `CARR-1`) can be used.  Between 1 and 10 units should be queried when using the `bmUnit` level. (optional)
fuel_type = ['fuel_type_example'] # list[str] | The fuel type to query when using the `fuelType` level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Fourteen-day generation capacity forecast (FOU2T14D)
    api_response = api_instance.get_forecast_availability_daily(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_availability_daily: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| The filter level for the forecast. This can be one of the following:  - &#x60;total&#x60;: the total forecast for the given time period.  - &#x60;bmUnit&#x60;: the forecast for each specified BM unit.  - &#x60;fuelType&#x60;: the forecast aggregated, and optionally filtered by fuel type. | [optional] 
 **bm_unit** | [**list[str]**](str.md)| The BM units to query. Add each unit separately. Either the Elexon ID (Eg: &#x60;T_CARR-1&#x60;) or National Grid ID (Eg: &#x60;CARR-1&#x60;) can be used.  Between 1 and 10 units should be queried when using the &#x60;bmUnit&#x60; level. | [optional] 
 **fuel_type** | [**list[str]**](str.md)| The fuel type to query when using the &#x60;fuelType&#x60; level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_availability_daily_evolution_forecastdate_forecastdate**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily get_forecast_availability_daily_evolution_forecastdate_forecastdate(forecast_date, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)

This endpoint provides the evolution of all daily generation forecasts over time for a given Forecast Date.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
forecast_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The forecast date for the filter. This must be in the format yyyy-MM-dd.
level = 'level_example' # str | The filter level for the forecast. This can be one of the following:  - `total`: the total forecast for the given time period.  - `bmUnit`: the forecast for each specified BM unit.  - `fuelType`: the forecast aggregated, and optionally filtered by fuel type. (optional)
bm_unit = ['bm_unit_example'] # list[str] | The BM units to query. Add each unit separately. Either the Elexon ID (Eg: `T_CARR-1`) or National Grid ID (Eg: `CARR-1`) can be used.  Between 1 and 10 units should be queried when using the `bmUnit` level. (optional)
fuel_type = ['fuel_type_example'] # list[str] | The fuel type to query when using the `fuelType` level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)
    api_response = api_instance.get_forecast_availability_daily_evolution_forecastdate_forecastdate(forecast_date, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_availability_daily_evolution_forecastdate_forecastdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| Format - date (as full-date in RFC3339). The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **level** | **str**| The filter level for the forecast. This can be one of the following:  - &#x60;total&#x60;: the total forecast for the given time period.  - &#x60;bmUnit&#x60;: the forecast for each specified BM unit.  - &#x60;fuelType&#x60;: the forecast aggregated, and optionally filtered by fuel type. | [optional] 
 **bm_unit** | [**list[str]**](str.md)| The BM units to query. Add each unit separately. Either the Elexon ID (Eg: &#x60;T_CARR-1&#x60;) or National Grid ID (Eg: &#x60;CARR-1&#x60;) can be used.  Between 1 and 10 units should be queried when using the &#x60;bmUnit&#x60; level. | [optional] 
 **fuel_type** | [**list[str]**](str.md)| The fuel type to query when using the &#x60;fuelType&#x60; level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_availability_daily_history_publishtime_publishtime**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily get_forecast_availability_daily_history_publishtime_publishtime(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

History of the fourteen-day generation capacity forecast (FOU2T14D)

This endpoint provides the latest fourteen-day generation forecast from a given DateTime

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). The UTC publish time to query. This should be in the format yyyy-MM-ddT:HH:mm:ssZ.
level = 'level_example' # str | The filter level for the forecast. This can be one of the following:  - `total`: the total forecast for the given time period.  - `bmUnit`: the forecast for each specified BM unit.  - `fuelType`: the forecast aggregated, and optionally filtered by fuel type. (optional)
bm_unit = ['bm_unit_example'] # list[str] | The BM units to query. Add each unit separately. Either the Elexon ID (Eg: `T_CARR-1`) or National Grid ID (Eg: `CARR-1`) can be used.  Between 1 and 10 units should be queried when using the `bmUnit` level. (optional)
fuel_type = ['fuel_type_example'] # list[str] | The fuel type to query when using the `fuelType` level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the fourteen-day generation capacity forecast (FOU2T14D)
    api_response = api_instance.get_forecast_availability_daily_history_publishtime_publishtime(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_availability_daily_history_publishtime_publishtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**| Format - date-time (as date-time in RFC3339). The UTC publish time to query. This should be in the format yyyy-MM-ddT:HH:mm:ssZ. | 
 **level** | **str**| The filter level for the forecast. This can be one of the following:  - &#x60;total&#x60;: the total forecast for the given time period.  - &#x60;bmUnit&#x60;: the forecast for each specified BM unit.  - &#x60;fuelType&#x60;: the forecast aggregated, and optionally filtered by fuel type. | [optional] 
 **bm_unit** | [**list[str]**](str.md)| The BM units to query. Add each unit separately. Either the Elexon ID (Eg: &#x60;T_CARR-1&#x60;) or National Grid ID (Eg: &#x60;CARR-1&#x60;) can be used.  Between 1 and 10 units should be queried when using the &#x60;bmUnit&#x60; level. | [optional] 
 **fuel_type** | [**list[str]**](str.md)| The fuel type to query when using the &#x60;fuelType&#x60; level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_availability_summary14d**
> list[InsightsApiModelsResponsesGenerationAggregatedForecast] get_forecast_availability_summary14d(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. Use forecast/availability/daily instead

This endpoint provides a summary of generation forecast data aggregated by forecast date,  intended for visualisation purposes. Use other availability forecast endpoints for full dataset access.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. Use forecast/availability/daily instead
    api_response = api_instance.get_forecast_availability_summary14d(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_availability_summary14d: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**list[InsightsApiModelsResponsesGenerationAggregatedForecast]**](InsightsApiModelsResponsesGenerationAggregatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_availability_summary3yw**
> list[InsightsApiModelsResponsesGenerationAggregatedForecast] get_forecast_availability_summary3yw(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. Use forecast/availability/weekly instead

This endpoint provides a summary of generation forecast data aggregated by forecast date,  intended for visualisation purposes. Use other availability forecast endpoints for full dataset access.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. Use forecast/availability/weekly instead
    api_response = api_instance.get_forecast_availability_summary3yw(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_availability_summary3yw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**list[InsightsApiModelsResponsesGenerationAggregatedForecast]**](InsightsApiModelsResponsesGenerationAggregatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_availability_weekly**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly get_forecast_availability_weekly(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Three-year generation capacity forecast (FOU2T3YW)

This endpoint provides the latest three-year generation forecast

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
level = 'level_example' # str | The filter level for the forecast. This can be one of the following:  - `total`: the total forecast for the given time period.  - `bmUnit`: the forecast for each specified BM unit.  - `fuelType`: the forecast aggregated, and optionally filtered by fuel type. (optional)
bm_unit = ['bm_unit_example'] # list[str] | The BM units to query. Add each unit separately. Either the Elexon ID (Eg: `T_CARR-1`) or National Grid ID (Eg: `CARR-1`) can be used.  Between 1 and 10 units should be queried when using the `bmUnit` level. (optional)
fuel_type = ['fuel_type_example'] # list[str] | The fuel type to query when using the `fuelType` level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Three-year generation capacity forecast (FOU2T3YW)
    api_response = api_instance.get_forecast_availability_weekly(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_availability_weekly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| The filter level for the forecast. This can be one of the following:  - &#x60;total&#x60;: the total forecast for the given time period.  - &#x60;bmUnit&#x60;: the forecast for each specified BM unit.  - &#x60;fuelType&#x60;: the forecast aggregated, and optionally filtered by fuel type. | [optional] 
 **bm_unit** | [**list[str]**](str.md)| The BM units to query. Add each unit separately. Either the Elexon ID (Eg: &#x60;T_CARR-1&#x60;) or National Grid ID (Eg: &#x60;CARR-1&#x60;) can be used.  Between 1 and 10 units should be queried when using the &#x60;bmUnit&#x60; level. | [optional] 
 **fuel_type** | [**list[str]**](str.md)| The fuel type to query when using the &#x60;fuelType&#x60; level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_availability_weekly_evolution_year_year_week_week**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly get_forecast_availability_weekly_evolution_year_year_week_week(year, week, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Evolution of the three-year generation capacity forecast over time (FOU2T3YW)

This endpoint provides all weekly generation forecasts over time for a given Year and Week

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
year = 56 # int | Format - int32. The forecast year for the filter.
week = 56 # int | Format - int32. The forecast week for the filter.
level = 'level_example' # str | The filter level for the forecast. This can be one of the following:  - `total`: the total forecast for the given time period.  - `bmUnit`: the forecast for each specified BM unit.  - `fuelType`: the forecast aggregated, and optionally filtered by fuel type. (optional)
bm_unit = ['bm_unit_example'] # list[str] | The BM units to query. Add each unit separately. Either the Elexon ID (Eg: `T_CARR-1`) or National Grid ID (Eg: `CARR-1`) can be used.  Between 1 and 10 units should be queried when using the `bmUnit` level. (optional)
fuel_type = ['fuel_type_example'] # list[str] | The fuel type to query when using the `fuelType` level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the three-year generation capacity forecast over time (FOU2T3YW)
    api_response = api_instance.get_forecast_availability_weekly_evolution_year_year_week_week(year, week, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_availability_weekly_evolution_year_year_week_week: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Format - int32. The forecast year for the filter. | 
 **week** | **int**| Format - int32. The forecast week for the filter. | 
 **level** | **str**| The filter level for the forecast. This can be one of the following:  - &#x60;total&#x60;: the total forecast for the given time period.  - &#x60;bmUnit&#x60;: the forecast for each specified BM unit.  - &#x60;fuelType&#x60;: the forecast aggregated, and optionally filtered by fuel type. | [optional] 
 **bm_unit** | [**list[str]**](str.md)| The BM units to query. Add each unit separately. Either the Elexon ID (Eg: &#x60;T_CARR-1&#x60;) or National Grid ID (Eg: &#x60;CARR-1&#x60;) can be used.  Between 1 and 10 units should be queried when using the &#x60;bmUnit&#x60; level. | [optional] 
 **fuel_type** | [**list[str]**](str.md)| The fuel type to query when using the &#x60;fuelType&#x60; level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_availability_weekly_history_publishtime_publishtime**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly get_forecast_availability_weekly_history_publishtime_publishtime(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

History of the three-year generation capacity forecast (FOU2T3YW)

This endpoint provides the latest three-year forecast from a given DateTime

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). The UTC publish time to query. This should be in the format yyyy-MM-ddT:HH:mm:ssZ.
level = 'level_example' # str | The filter level for the forecast. This can be one of the following:  - `total`: the total forecast for the given time period.  - `bmUnit`: the forecast for each specified BM unit.  - `fuelType`: the forecast aggregated, and optionally filtered by fuel type. (optional)
bm_unit = ['bm_unit_example'] # list[str] | The BM units to query. Add each unit separately. Either the Elexon ID (Eg: `T_CARR-1`) or National Grid ID (Eg: `CARR-1`) can be used.  Between 1 and 10 units should be queried when using the `bmUnit` level. (optional)
fuel_type = ['fuel_type_example'] # list[str] | The fuel type to query when using the `fuelType` level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the three-year generation capacity forecast (FOU2T3YW)
    api_response = api_instance.get_forecast_availability_weekly_history_publishtime_publishtime(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_availability_weekly_history_publishtime_publishtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**| Format - date-time (as date-time in RFC3339). The UTC publish time to query. This should be in the format yyyy-MM-ddT:HH:mm:ssZ. | 
 **level** | **str**| The filter level for the forecast. This can be one of the following:  - &#x60;total&#x60;: the total forecast for the given time period.  - &#x60;bmUnit&#x60;: the forecast for each specified BM unit.  - &#x60;fuelType&#x60;: the forecast aggregated, and optionally filtered by fuel type. | [optional] 
 **bm_unit** | [**list[str]**](str.md)| The BM units to query. Add each unit separately. Either the Elexon ID (Eg: &#x60;T_CARR-1&#x60;) or National Grid ID (Eg: &#x60;CARR-1&#x60;) can be used.  Between 1 and 10 units should be queried when using the &#x60;bmUnit&#x60; level. | [optional] 
 **fuel_type** | [**list[str]**](str.md)| The fuel type to query when using the &#x60;fuelType&#x60; level. Add each fuel type separately. If no fuel types are supplied, all fuel types will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_day_ahead_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration get_forecast_generation_day_ahead_from_from_to_to(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Day-ahead aggregated generation (DAG/B1430)

This endpoint provides day-ahead aggregated generation data filtered by settlement date.                This API endpoint has a maximum range of 7 days.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
settlement_period_from = 56 # int | Format - int32. (optional)
settlement_period_to = 56 # int | Format - int32. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Day-ahead aggregated generation (DAG/B1430)
    api_response = api_instance.get_forecast_generation_day_ahead_from_from_to_to(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_day_ahead_from_from_to_to: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast get_forecast_generation_wind(format=format)

Current wind generation forecast (WINDFOR)

This endpoint provides the latest wind generation forecast data. This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30. Results are filtered by a range of DateTime parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Current wind generation forecast (WINDFOR)
    api_response = api_instance.get_forecast_generation_wind(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind_and_solar_day_ahead_from_from_to_to_processtype**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar get_forecast_generation_wind_and_solar_day_ahead_from_from_to_to_processtype(_from, to, process_type, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Day-ahead generation forecast for wind and solar (DGWS/B1440)

This endpoint provides day-ahead forecast generation data for wind and solar.                This endpoint filters by startTime and provides a maximum data output range of 7 days.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
process_type = 'process_type_example' # str | 
settlement_period_from = 56 # int | Format - int32. (optional)
settlement_period_to = 56 # int | Format - int32. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Day-ahead generation forecast for wind and solar (DGWS/B1440)
    api_response = api_instance.get_forecast_generation_wind_and_solar_day_ahead_from_from_to_to_processtype(_from, to, process_type, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind_and_solar_day_ahead_from_from_to_to_processtype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **process_type** | **str**|  | 
 **settlement_period_from** | **int**| Format - int32. | [optional] 
 **settlement_period_to** | **int**| Format - int32. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind_earliest_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast get_forecast_generation_wind_earliest_from_from_to_to(_from, to, format=format)

Historic view of the earliest forecasted wind generation (WINDFOR)

This endpoint provides the eariest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic view of the earliest forecasted wind generation (WINDFOR)
    api_response = api_instance.get_forecast_generation_wind_earliest_from_from_to_to(_from, to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind_earliest_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind_earliest_stream_from_from_to_to**
> list[InsightsApiModelsServiceWindGenerationForecastRow] get_forecast_generation_wind_earliest_stream_from_from_to_to(_from, to)

Historic view of the earliest forecasted wind generation (WINDFOR) stream

This endpoint provides the earliest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.  This endpoint has an optimised JSON payload and is aimed at frequent requests for the wind generation forecast data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).

try:
    # Historic view of the earliest forecasted wind generation (WINDFOR) stream
    api_response = api_instance.get_forecast_generation_wind_earliest_stream_from_from_to_to(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind_earliest_stream_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | 

### Return type

[**list[InsightsApiModelsServiceWindGenerationForecastRow]**](InsightsApiModelsServiceWindGenerationForecastRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind_evolution_starttime_starttime**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast get_forecast_generation_wind_evolution_starttime_starttime(start_time, format=format)

Evolution of the wind generation forecast over time (WINDFOR)

This endpoint provides the evolution wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the wind generation forecast over time (WINDFOR)
    api_response = api_instance.get_forecast_generation_wind_evolution_starttime_starttime(start_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind_evolution_starttime_starttime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind_history_publishtime_publishtime**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast get_forecast_generation_wind_history_publishtime_publishtime(publish_time, format=format)

History of the wind generation forecast (WINDFOR)

This endpoint provides the historical wind generation forecast data. This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the wind generation forecast (WINDFOR)
    api_response = api_instance.get_forecast_generation_wind_history_publishtime_publishtime(publish_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind_history_publishtime_publishtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind_latest_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast get_forecast_generation_wind_latest_from_from_to_to(_from, to, format=format)

Historic view of the latest forecasted wind generation (WINDFOR)

This endpoint provides the latest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic view of the latest forecasted wind generation (WINDFOR)
    api_response = api_instance.get_forecast_generation_wind_latest_from_from_to_to(_from, to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind_latest_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind_latest_stream_from_from_to_to**
> list[InsightsApiModelsServiceWindGenerationForecastRow] get_forecast_generation_wind_latest_stream_from_from_to_to(_from, to)

Historic view of the latest forecasted wind generation (WINDFOR) stream

This endpoint provides the latest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.  This endpoint has an optimised JSON payload and is aimed at frequent requests for the wind generation forecast data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).

try:
    # Historic view of the latest forecasted wind generation (WINDFOR) stream
    api_response = api_instance.get_forecast_generation_wind_latest_stream_from_from_to_to(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind_latest_stream_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | 

### Return type

[**list[InsightsApiModelsServiceWindGenerationForecastRow]**](InsightsApiModelsServiceWindGenerationForecastRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_generation_wind_peak**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast get_forecast_generation_wind_peak(_from=_from, to=to, format=format)

Peak wind generation forecast for each day (WINDFOR)

This endpoint provides the peak wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenerationForecastApi()
_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). The start of the requested date range. (optional)
to = '2013-10-20' # date | Format - date (as full-date in RFC3339). The end of the requested date range. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Peak wind generation forecast for each day (WINDFOR)
    api_response = api_instance.get_forecast_generation_wind_peak(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->get_forecast_generation_wind_peak: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Format - date (as full-date in RFC3339). The start of the requested date range. | [optional] 
 **to** | **date**| Format - date (as full-date in RFC3339). The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

