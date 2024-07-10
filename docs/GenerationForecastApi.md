# swagger_client.GenerationForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_availability_daily_evolution_get**](GenerationForecastApi.md#forecast_availability_daily_evolution_get) | **GET** /forecast/availability/daily/evolution | Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)
[**forecast_availability_daily_get**](GenerationForecastApi.md#forecast_availability_daily_get) | **GET** /forecast/availability/daily | Fourteen-day generation capacity forecast (FOU2T14D)
[**forecast_availability_daily_history_get**](GenerationForecastApi.md#forecast_availability_daily_history_get) | **GET** /forecast/availability/daily/history | History of the fourteen-day generation capacity forecast (FOU2T14D)
[**forecast_availability_summary14_d_get**](GenerationForecastApi.md#forecast_availability_summary14_d_get) | **GET** /forecast/availability/summary/14D | Down-sampled fourteen-day generation forecast (FOU2T14D)
[**forecast_availability_summary3_yw_get**](GenerationForecastApi.md#forecast_availability_summary3_yw_get) | **GET** /forecast/availability/summary/3YW | Down-sampled three-year generation forecast (FOU2T3YW)
[**forecast_availability_weekly_evolution_get**](GenerationForecastApi.md#forecast_availability_weekly_evolution_get) | **GET** /forecast/availability/weekly/evolution | Evolution of the three-year generation capacity forecast over time (FOU2T3YW)
[**forecast_availability_weekly_get**](GenerationForecastApi.md#forecast_availability_weekly_get) | **GET** /forecast/availability/weekly | Three-year generation capacity forecast (FOU2T3YW)
[**forecast_availability_weekly_history_get**](GenerationForecastApi.md#forecast_availability_weekly_history_get) | **GET** /forecast/availability/weekly/history | History of the three-year generation capacity forecast (FOU2T3YW)
[**forecast_generation_day_ahead_get**](GenerationForecastApi.md#forecast_generation_day_ahead_get) | **GET** /forecast/generation/day-ahead | Day-ahead aggregated generation (DAG/B1430)
[**forecast_generation_wind_and_solar_day_ahead_get**](GenerationForecastApi.md#forecast_generation_wind_and_solar_day_ahead_get) | **GET** /forecast/generation/wind-and-solar/day-ahead | Day-ahead generation forecast for wind and solar (DGWS/B1440)
[**forecast_generation_wind_earliest_get**](GenerationForecastApi.md#forecast_generation_wind_earliest_get) | **GET** /forecast/generation/wind/earliest | Historic view of the earliest forecasted wind generation (WINDFOR)
[**forecast_generation_wind_earliest_stream_get**](GenerationForecastApi.md#forecast_generation_wind_earliest_stream_get) | **GET** /forecast/generation/wind/earliest/stream | Historic view of the earliest forecasted wind generation (WINDFOR) stream
[**forecast_generation_wind_evolution_get**](GenerationForecastApi.md#forecast_generation_wind_evolution_get) | **GET** /forecast/generation/wind/evolution | Evolution of the wind generation forecast over time (WINDFOR)
[**forecast_generation_wind_get**](GenerationForecastApi.md#forecast_generation_wind_get) | **GET** /forecast/generation/wind | Current wind generation forecast (WINDFOR)
[**forecast_generation_wind_history_get**](GenerationForecastApi.md#forecast_generation_wind_history_get) | **GET** /forecast/generation/wind/history | History of the wind generation forecast (WINDFOR)
[**forecast_generation_wind_latest_get**](GenerationForecastApi.md#forecast_generation_wind_latest_get) | **GET** /forecast/generation/wind/latest | Historic view of the latest forecasted wind generation (WINDFOR)
[**forecast_generation_wind_latest_stream_get**](GenerationForecastApi.md#forecast_generation_wind_latest_stream_get) | **GET** /forecast/generation/wind/latest/stream | Historic view of the latest forecasted wind generation (WINDFOR) stream
[**forecast_generation_wind_peak_get**](GenerationForecastApi.md#forecast_generation_wind_peak_get) | **GET** /forecast/generation/wind/peak | Peak wind generation forecast for each day (WINDFOR)

# **forecast_availability_daily_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily forecast_availability_daily_evolution_get(forecast_date, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)

This endpoint provides the evolution of all daily generation forecasts over time for a given Forecast Date.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
forecast_date = '2013-10-20'  # date | The forecast date for the filter. This must be in the format yyyy-MM-dd.
level = 'level_example'  # str |  (optional)
bm_unit = ['bm_unit_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)
    api_response = api_instance.forecast_availability_daily_evolution_get(forecast_date, level=level, bm_unit=bm_unit,
                                                                          fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_availability_daily_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **level** | **str**|  | [optional] 
 **bm_unit** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_availability_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily forecast_availability_daily_get(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Fourteen-day generation capacity forecast (FOU2T14D)

This endpoint provides the latest fourteen-day generation forecast

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
level = 'level_example'  # str |  (optional)
bm_unit = ['bm_unit_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Fourteen-day generation capacity forecast (FOU2T14D)
    api_response = api_instance.forecast_availability_daily_get(level=level, bm_unit=bm_unit, fuel_type=fuel_type,
                                                                format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_availability_daily_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**|  | [optional] 
 **bm_unit** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_availability_daily_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily forecast_availability_daily_history_get(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

History of the fourteen-day generation capacity forecast (FOU2T14D)

This endpoint provides the latest fourteen-day generation forecast from a given DateTime

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
publish_time = '2013-10-20T19:20:30+01:00'  # datetime | 
level = 'level_example'  # str |  (optional)
bm_unit = ['bm_unit_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the fourteen-day generation capacity forecast (FOU2T14D)
    api_response = api_instance.forecast_availability_daily_history_get(publish_time, level=level, bm_unit=bm_unit,
                                                                        fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_availability_daily_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **level** | **str**|  | [optional] 
 **bm_unit** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_availability_summary14_d_get**
> list[InsightsApiModelsResponsesGenerationAggregatedForecast] forecast_availability_summary14_d_get(format=format)

Down-sampled fourteen-day generation forecast (FOU2T14D)

This endpoint provides a summary of generation forecast data aggregated by forecast date,  intended for visualisation purposes. Use other availability forecast endpoints for full dataset access.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Down-sampled fourteen-day generation forecast (FOU2T14D)
    api_response = api_instance.forecast_availability_summary14_d_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_availability_summary14_d_get: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_availability_summary3_yw_get**
> list[InsightsApiModelsResponsesGenerationAggregatedForecast] forecast_availability_summary3_yw_get(format=format)

Down-sampled three-year generation forecast (FOU2T3YW)

This endpoint provides a summary of generation forecast data aggregated by forecast date,  intended for visualisation purposes. Use other availability forecast endpoints for full dataset access.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Down-sampled three-year generation forecast (FOU2T3YW)
    api_response = api_instance.forecast_availability_summary3_yw_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_availability_summary3_yw_get: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_availability_weekly_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly forecast_availability_weekly_evolution_get(year, week, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Evolution of the three-year generation capacity forecast over time (FOU2T3YW)

This endpoint provides all weekly generation forecasts over time for a given Year and Week

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
year = 56  # int | 
week = 56  # int | 
level = 'level_example'  # str |  (optional)
bm_unit = ['bm_unit_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the three-year generation capacity forecast over time (FOU2T3YW)
    api_response = api_instance.forecast_availability_weekly_evolution_get(year, week, level=level, bm_unit=bm_unit,
                                                                           fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_availability_weekly_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 
 **week** | **int**|  | 
 **level** | **str**|  | [optional] 
 **bm_unit** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_availability_weekly_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly forecast_availability_weekly_get(level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

Three-year generation capacity forecast (FOU2T3YW)

This endpoint provides the latest three-year generation forecast

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
level = 'level_example'  # str |  (optional)
bm_unit = ['bm_unit_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Three-year generation capacity forecast (FOU2T3YW)
    api_response = api_instance.forecast_availability_weekly_get(level=level, bm_unit=bm_unit, fuel_type=fuel_type,
                                                                 format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_availability_weekly_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**|  | [optional] 
 **bm_unit** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_availability_weekly_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly forecast_availability_weekly_history_get(publish_time, level=level, bm_unit=bm_unit, fuel_type=fuel_type, format=format)

History of the three-year generation capacity forecast (FOU2T3YW)

This endpoint provides the latest three-year forecast from a given DateTime

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
publish_time = '2013-10-20T19:20:30+01:00'  # datetime | 
level = 'level_example'  # str |  (optional)
bm_unit = ['bm_unit_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the three-year generation capacity forecast (FOU2T3YW)
    api_response = api_instance.forecast_availability_weekly_history_get(publish_time, level=level, bm_unit=bm_unit,
                                                                         fuel_type=fuel_type, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_availability_weekly_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **level** | **str**|  | [optional] 
 **bm_unit** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration forecast_generation_day_ahead_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Day-ahead aggregated generation (DAG/B1430)

This endpoint provides day-ahead aggregated generation data filtered by settlement date.                This API endpoint has a maximum range of 7 days.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
settlement_period_from = 56  # int |  (optional)
settlement_period_to = 56  # int |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Day-ahead aggregated generation (DAG/B1430)
    api_response = api_instance.forecast_generation_day_ahead_get(_from, to,
                                                                  settlement_period_from=settlement_period_from,
                                                                  settlement_period_to=settlement_period_to,
                                                                  format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_day_ahead_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **settlement_period_from** | **int**|  | [optional] 
 **settlement_period_to** | **int**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_and_solar_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar forecast_generation_wind_and_solar_day_ahead_get(_from, to, process_type, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Day-ahead generation forecast for wind and solar (DGWS/B1440)

This endpoint provides day-ahead forecast generation data for wind and solar.                This endpoint filters by startTime and provides a maximum data output range of 7 days.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
process_type = 'process_type_example'  # str | 
settlement_period_from = 56  # int |  (optional)
settlement_period_to = 56  # int |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Day-ahead generation forecast for wind and solar (DGWS/B1440)
    api_response = api_instance.forecast_generation_wind_and_solar_day_ahead_get(_from, to, process_type,
                                                                                 settlement_period_from=settlement_period_from,
                                                                                 settlement_period_to=settlement_period_to,
                                                                                 format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_and_solar_day_ahead_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **process_type** | **str**|  | 
 **settlement_period_from** | **int**|  | [optional] 
 **settlement_period_to** | **int**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_earliest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_earliest_get(_from, to, format=format)

Historic view of the earliest forecasted wind generation (WINDFOR)

This endpoint provides the eariest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic view of the earliest forecasted wind generation (WINDFOR)
    api_response = api_instance.forecast_generation_wind_earliest_get(_from, to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_earliest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_earliest_stream_get**
> list[InsightsApiModelsServiceWindGenerationForecastRow] forecast_generation_wind_earliest_stream_get(_from, to)

Historic view of the earliest forecasted wind generation (WINDFOR) stream

This endpoint provides the earliest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.  This endpoint has an optimised JSON payload and is aimed at frequent requests for the wind generation forecast data.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 

try:
    # Historic view of the earliest forecasted wind generation (WINDFOR) stream
    api_response = api_instance.forecast_generation_wind_earliest_stream_get(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_earliest_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 

### Return type

[**list[InsightsApiModelsServiceWindGenerationForecastRow]**](InsightsApiModelsServiceWindGenerationForecastRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_evolution_get(start_time, format=format)

Evolution of the wind generation forecast over time (WINDFOR)

This endpoint provides the evolution wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
start_time = '2013-10-20T19:20:30+01:00'  # datetime | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the wind generation forecast over time (WINDFOR)
    api_response = api_instance.forecast_generation_wind_evolution_get(start_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_get(format=format)

Current wind generation forecast (WINDFOR)

This endpoint provides the latest wind generation forecast data. This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30. Results are filtered by a range of DateTime parameters.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Current wind generation forecast (WINDFOR)
    api_response = api_instance.forecast_generation_wind_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_get: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_history_get(publish_time, format=format)

History of the wind generation forecast (WINDFOR)

This endpoint provides the historical wind generation forecast data. This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
publish_time = '2013-10-20T19:20:30+01:00'  # datetime | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the wind generation forecast (WINDFOR)
    api_response = api_instance.forecast_generation_wind_history_get(publish_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_latest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_latest_get(_from, to, format=format)

Historic view of the latest forecasted wind generation (WINDFOR)

This endpoint provides the latest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic view of the latest forecasted wind generation (WINDFOR)
    api_response = api_instance.forecast_generation_wind_latest_get(_from, to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_latest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_latest_stream_get**
> list[InsightsApiModelsServiceWindGenerationForecastRow] forecast_generation_wind_latest_stream_get(_from, to)

Historic view of the latest forecasted wind generation (WINDFOR) stream

This endpoint provides the latest wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.  This endpoint has an optimised JSON payload and is aimed at frequent requests for the wind generation forecast data.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 

try:
    # Historic view of the latest forecasted wind generation (WINDFOR) stream
    api_response = api_instance.forecast_generation_wind_latest_stream_get(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_latest_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 

### Return type

[**list[InsightsApiModelsServiceWindGenerationForecastRow]**](InsightsApiModelsServiceWindGenerationForecastRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_generation_wind_peak_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast forecast_generation_wind_peak_get(_from=_from, to=to, format=format)

Peak wind generation forecast for each day (WINDFOR)

This endpoint provides the peak wind generation forecast data.  This provides wind generation forecast for wind farms which are visible to the ESO and have operational metering.  Updated data is published by NGESO up to 8 times a day at 03:30, 05:30, 08:30, 10:30, 12:30, 16:30, 19:30 and 23:30.  Results are filtered by a range of DateTime parameters.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.GenerationForecastApi()
_from = '2013-10-20'  # date | The start of the requested date range. (optional)
to = '2013-10-20'  # date | The end of the requested date range. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Peak wind generation forecast for each day (WINDFOR)
    api_response = api_instance.forecast_generation_wind_peak_get(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationForecastApi->forecast_generation_wind_peak_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| The start of the requested date range. | [optional] 
 **to** | **date**| The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

