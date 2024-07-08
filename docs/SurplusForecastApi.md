# swagger_client.SurplusForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_surplus_daily_evolution_get**](SurplusForecastApi.md#forecast_surplus_daily_evolution_get) | **GET** /forecast/surplus/daily/evolution | Evolution daily surplus forecast (OCNMFD)
[**forecast_surplus_daily_get**](SurplusForecastApi.md#forecast_surplus_daily_get) | **GET** /forecast/surplus/daily | Daily surplus forecast (OCNMFD)
[**forecast_surplus_daily_history_get**](SurplusForecastApi.md#forecast_surplus_daily_history_get) | **GET** /forecast/surplus/daily/history | Historical daily surplus forecast (OCNMFD)
[**forecast_surplus_weekly_evolution_get**](SurplusForecastApi.md#forecast_surplus_weekly_evolution_get) | **GET** /forecast/surplus/weekly/evolution | Evolution weekly surplus forecast (OCNMFW, OCNMF3Y)
[**forecast_surplus_weekly_get**](SurplusForecastApi.md#forecast_surplus_weekly_get) | **GET** /forecast/surplus/weekly | Weekly surplus forecast (OCNMFW, OCNMF3Y)
[**forecast_surplus_weekly_history_get**](SurplusForecastApi.md#forecast_surplus_weekly_history_get) | **GET** /forecast/surplus/weekly/history | Historical weekly surplus forecast (OCNMFW, OCNMF3Y)

# **forecast_surplus_daily_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily forecast_surplus_daily_evolution_get(forecast_date, format=format)

Evolution daily surplus forecast (OCNMFD)

This endpoint provides the daily evolution Generating Plant Operating Surplus covering 2 days ahead to 14 days ahead in MW values.  The Daily API outputs the latest published data for daily surplus forecast for D+2 to D+14.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SurplusForecastApi()
forecast_date = '2013-10-20' # date | The forecast date for the filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution daily surplus forecast (OCNMFD)
    api_response = api_instance.forecast_surplus_daily_evolution_get(forecast_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurplusForecastApi->forecast_surplus_daily_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_surplus_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily forecast_surplus_daily_get(format=format)

Daily surplus forecast (OCNMFD)

This endpoint provides the Generating Plant Operating Surplus covering 2 days ahead to 14 days ahead in MW values.  The Daily API outputs the latest published data for daily surplus forecast for D+2 t D+14

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SurplusForecastApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Daily surplus forecast (OCNMFD)
    api_response = api_instance.forecast_surplus_daily_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurplusForecastApi->forecast_surplus_daily_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_surplus_daily_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily forecast_surplus_daily_history_get(publish_time, format=format)

Historical daily surplus forecast (OCNMFD)

This endpoint provides the historic Generating Plant Operating Surplus covering 2 days ahead to 14 days ahead in MW values.  The historic API outputs the latest published data for historic daily surplus forecast for D+2 to D+14

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SurplusForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historical daily surplus forecast (OCNMFD)
    api_response = api_instance.forecast_surplus_daily_history_get(publish_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurplusForecastApi->forecast_surplus_daily_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_surplus_weekly_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly forecast_surplus_weekly_evolution_get(year, week, range=range, format=format)

Evolution weekly surplus forecast (OCNMFW, OCNMF3Y)

This endpoint provides the evolution Generating Plant Operating Surplus  covering 2 weeks ahead to 156 weeks ahead in MW values.  The weekly API outputs the latest published data for weekly surplus forecast for W+2 to W+156

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SurplusForecastApi()
year = 56 # int | 
week = 56 # int | 
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution weekly surplus forecast (OCNMFW, OCNMF3Y)
    api_response = api_instance.forecast_surplus_weekly_evolution_get(year, week, range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurplusForecastApi->forecast_surplus_weekly_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 
 **week** | **int**|  | 
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_surplus_weekly_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly forecast_surplus_weekly_get(range=range, format=format)

Weekly surplus forecast (OCNMFW, OCNMF3Y)

This endpoint provides the Generating Plant Operating Surplus covering 2 weeks ahead to 156 weeks ahead in MW values.  The weekly API outputs the latest published data for weekly surplus forecast for W+2 to W+156

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SurplusForecastApi()
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Weekly surplus forecast (OCNMFW, OCNMF3Y)
    api_response = api_instance.forecast_surplus_weekly_get(range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurplusForecastApi->forecast_surplus_weekly_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_surplus_weekly_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly forecast_surplus_weekly_history_get(publish_time, range=range, format=format)

Historical weekly surplus forecast (OCNMFW, OCNMF3Y)

This endpoint provides the historic Generating Plant Operating Surplus covering 2 weeks ahead to 156 weeks ahead in MW values.  The weekly API outputs the latest published data for weekly surplus forecast for W+2 to W+156.  Historical published data of weekly surplus forecasts for a given publish date in the 2-156 week dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SurplusForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | 
range = 'range_example' # str |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historical weekly surplus forecast (OCNMFW, OCNMF3Y)
    api_response = api_instance.forecast_surplus_weekly_history_get(publish_time, range=range, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurplusForecastApi->forecast_surplus_weekly_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **range** | **str**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

