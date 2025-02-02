# elexonpy.MarginForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forecast_margin_daily**](MarginForecastApi.md#get_forecast_margin_daily) | **GET** /forecast/margin/daily | Daily margin forecast (OCNMFD2)
[**get_forecast_margin_daily_evolution_forecastdate_forecastdate**](MarginForecastApi.md#get_forecast_margin_daily_evolution_forecastdate_forecastdate) | **GET** /forecast/margin/daily/evolution | Evolution daily margin forecast (OCNMFD2)
[**get_forecast_margin_daily_history_publishtime_publishtime**](MarginForecastApi.md#get_forecast_margin_daily_history_publishtime_publishtime) | **GET** /forecast/margin/daily/history | Historical daily margin forecast (OCNMFD2)
[**get_forecast_margin_weekly**](MarginForecastApi.md#get_forecast_margin_weekly) | **GET** /forecast/margin/weekly | Weekly margin forecast (OCNMFW2, OCNMF3Y2)
[**get_forecast_margin_weekly_evolution_year_year_week_week**](MarginForecastApi.md#get_forecast_margin_weekly_evolution_year_year_week_week) | **GET** /forecast/margin/weekly/evolution | Evolution daily margin forecast (OCNMFW2, OCNMF3Y2)
[**get_forecast_margin_weekly_history_publishtime_publishtime**](MarginForecastApi.md#get_forecast_margin_weekly_history_publishtime_publishtime) | **GET** /forecast/margin/weekly/history | Historical weekly margin forecast (OCNMFW2, OCNMF3Y2)

# **get_forecast_margin_daily**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily get_forecast_margin_daily(format=format)

Daily margin forecast (OCNMFD2)

This endpoint provides the Generating Plant Operating Margin covering 2 days ahead to 14 days ahead  in MW values. The Daily API outputs the latest published data for daily margin forecast for D+2 t D+14

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.MarginForecastApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Daily margin forecast (OCNMFD2)
    api_response = api_instance.get_forecast_margin_daily(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->get_forecast_margin_daily: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_margin_daily_evolution_forecastdate_forecastdate**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily get_forecast_margin_daily_evolution_forecastdate_forecastdate(forecast_date, format=format)

Evolution daily margin forecast (OCNMFD2)

This endpoint provides the daily evolution Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The Daily API outputs the latest published data for daily margin forecast for D+2 to D+14.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.MarginForecastApi()
forecast_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The forecast date for the filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution daily margin forecast (OCNMFD2)
    api_response = api_instance.get_forecast_margin_daily_evolution_forecastdate_forecastdate(forecast_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->get_forecast_margin_daily_evolution_forecastdate_forecastdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| Format - date (as full-date in RFC3339). The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_margin_daily_history_publishtime_publishtime**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily get_forecast_margin_daily_history_publishtime_publishtime(publish_time, format=format)

Historical daily margin forecast (OCNMFD2)

This endpoint provides the historic Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The historic API outputs the latest published data for historic daily margin forecast for D+2 to D+14

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.MarginForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historical daily margin forecast (OCNMFD2)
    api_response = api_instance.get_forecast_margin_daily_history_publishtime_publishtime(publish_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->get_forecast_margin_daily_history_publishtime_publishtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_margin_weekly**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly get_forecast_margin_weekly(range=range, format=format)

Weekly margin forecast (OCNMFW2, OCNMF3Y2)

This endpoint provides the Generating Plant Operating Margin covering 2 weeks ahead to 156 weeks ahead in MW values.  The weekly API outputs the latest published data for weekly margin forecast for W+2 to W+156

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.MarginForecastApi()
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Weekly margin forecast (OCNMFW2, OCNMF3Y2)
    api_response = api_instance.get_forecast_margin_weekly(range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->get_forecast_margin_weekly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_margin_weekly_evolution_year_year_week_week**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly get_forecast_margin_weekly_evolution_year_year_week_week(year, week, range=range, format=format)

Evolution daily margin forecast (OCNMFW2, OCNMF3Y2)

This endpoint provides the daily evolution Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The Daily API outputs the latest published data for daily margin forecast for D+2 t D+14

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.MarginForecastApi()
year = 56 # int | Format - int32.
week = 56 # int | Format - int32.
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution daily margin forecast (OCNMFW2, OCNMF3Y2)
    api_response = api_instance.get_forecast_margin_weekly_evolution_year_year_week_week(year, week, range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->get_forecast_margin_weekly_evolution_year_year_week_week: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Format - int32. | 
 **week** | **int**| Format - int32. | 
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_margin_weekly_history_publishtime_publishtime**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly get_forecast_margin_weekly_history_publishtime_publishtime(publish_time, range=range, format=format)

Historical weekly margin forecast (OCNMFW2, OCNMF3Y2)

This endpoint provides the weekly historic  Generating Plant Operating Margin.  This historic API output 2 weeks ahead to 156 weeks ahead in MW values

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.MarginForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historical weekly margin forecast (OCNMFW2, OCNMF3Y2)
    api_response = api_instance.get_forecast_margin_weekly_history_publishtime_publishtime(publish_time, range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->get_forecast_margin_weekly_history_publishtime_publishtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

