# swagger_client.MarginForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_margin_daily_evolution_get**](MarginForecastApi.md#forecast_margin_daily_evolution_get) | **GET** /forecast/margin/daily/evolution | Evolution daily margin forecast (OCNMFD2)
[**forecast_margin_daily_get**](MarginForecastApi.md#forecast_margin_daily_get) | **GET** /forecast/margin/daily | Daily margin forecast (OCNMFD2)
[**forecast_margin_daily_history_get**](MarginForecastApi.md#forecast_margin_daily_history_get) | **GET** /forecast/margin/daily/history | Historical daily margin forecast (OCNMFD2)
[**forecast_margin_weekly_evolution_get**](MarginForecastApi.md#forecast_margin_weekly_evolution_get) | **GET** /forecast/margin/weekly/evolution | Evolution daily margin forecast (OCNMFW2, OCNMF3Y2)
[**forecast_margin_weekly_get**](MarginForecastApi.md#forecast_margin_weekly_get) | **GET** /forecast/margin/weekly | Weekly margin forecast (OCNMFW2, OCNMF3Y2)
[**forecast_margin_weekly_history_get**](MarginForecastApi.md#forecast_margin_weekly_history_get) | **GET** /forecast/margin/weekly/history | Historical weekly margin forecast (OCNMFW2, OCNMF3Y2)

# **forecast_margin_daily_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily forecast_margin_daily_evolution_get(forecast_date, format=format)

Evolution daily margin forecast (OCNMFD2)

This endpoint provides the daily evolution Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The Daily API outputs the latest published data for daily margin forecast for D+2 to D+14.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarginForecastApi()
forecast_date = '2013-10-20' # date | The forecast date for the filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution daily margin forecast (OCNMFD2)
    api_response = api_instance.forecast_margin_daily_evolution_get(forecast_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->forecast_margin_daily_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_margin_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily forecast_margin_daily_get(format=format)

Daily margin forecast (OCNMFD2)

This endpoint provides the Generating Plant Operating Margin covering 2 days ahead to 14 days ahead  in MW values. The Daily API outputs the latest published data for daily margin forecast for D+2 t D+14

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarginForecastApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Daily margin forecast (OCNMFD2)
    api_response = api_instance.forecast_margin_daily_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->forecast_margin_daily_get: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_margin_daily_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily forecast_margin_daily_history_get(publish_time, format=format)

Historical daily margin forecast (OCNMFD2)

This endpoint provides the historic Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The historic API outputs the latest published data for historic daily margin forecast for D+2 to D+14

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarginForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historical daily margin forecast (OCNMFD2)
    api_response = api_instance.forecast_margin_daily_history_get(publish_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->forecast_margin_daily_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_margin_weekly_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly forecast_margin_weekly_evolution_get(year, week, range=range, format=format)

Evolution daily margin forecast (OCNMFW2, OCNMF3Y2)

This endpoint provides the daily evolution Generating Plant Operating Margin covering 2 days ahead to 14 days ahead in MW values.  The Daily API outputs the latest published data for daily margin forecast for D+2 t D+14

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarginForecastApi()
year = 56 # int | 
week = 56 # int | 
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution daily margin forecast (OCNMFW2, OCNMF3Y2)
    api_response = api_instance.forecast_margin_weekly_evolution_get(year, week, range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->forecast_margin_weekly_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 
 **week** | **int**|  | 
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_margin_weekly_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly forecast_margin_weekly_get(range=range, format=format)

Weekly margin forecast (OCNMFW2, OCNMF3Y2)

This endpoint provides the Generating Plant Operating Margin covering 2 weeks ahead to 156 weeks ahead in MW values.  The weekly API outputs the latest published data for weekly margin forecast for W+2 to W+156

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarginForecastApi()
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Weekly margin forecast (OCNMFW2, OCNMF3Y2)
    api_response = api_instance.forecast_margin_weekly_get(range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->forecast_margin_weekly_get: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_margin_weekly_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly forecast_margin_weekly_history_get(publish_time, range=range, format=format)

Historical weekly margin forecast (OCNMFW2, OCNMF3Y2)

This endpoint provides the weekly historic  Generating Plant Operating Margin.  This historic API output 2 weeks ahead to 156 weeks ahead in MW values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarginForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historical weekly margin forecast (OCNMFW2, OCNMF3Y2)
    api_response = api_instance.forecast_margin_weekly_history_get(publish_time, range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginForecastApi->forecast_margin_weekly_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

