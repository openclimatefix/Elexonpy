# swagger_client.IndicatedForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forecast_indicated_day_ahead**](IndicatedForecastApi.md#get_forecast_indicated_day_ahead) | **GET** /forecast/indicated/day-ahead | Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
[**get_forecast_indicated_day_ahead_evolution_settlementdate_settlementdate_set**](IndicatedForecastApi.md#get_forecast_indicated_day_ahead_evolution_settlementdate_settlementdate_set) | **GET** /forecast/indicated/day-ahead/evolution | Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
[**get_forecast_indicated_day_ahead_history_publishtime_publishtime**](IndicatedForecastApi.md#get_forecast_indicated_day_ahead_history_publishtime_publishtime) | **GET** /forecast/indicated/day-ahead/history | Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)

# **get_forecast_indicated_day_ahead**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast get_forecast_indicated_day_ahead(boundary=boundary, format=format)

Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)

This endpoint provides the latest forecast indicated day-ahead data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatedForecastApi()
boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
    api_response = api_instance.get_forecast_indicated_day_ahead(boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatedForecastApi->get_forecast_indicated_day_ahead: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_indicated_day_ahead_evolution_settlementdate_settlementdate_set**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast get_forecast_indicated_day_ahead_evolution_settlementdate_settlementdate_set(settlement_date, settlement_period, boundary=boundary, format=format)

Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)

This endpoint provides the forecast indicated day-ahead data over time for the specified settlement date and settlement period.    Date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatedForecastApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd.
settlement_period = [56] # list[int] | 
boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
    api_response = api_instance.get_forecast_indicated_day_ahead_evolution_settlementdate_settlementdate_set(settlement_date, settlement_period, boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatedForecastApi->get_forecast_indicated_day_ahead_evolution_settlementdate_settlementdate_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **settlement_period** | [**list[int]**](int.md)|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_indicated_day_ahead_history_publishtime_publishtime**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast get_forecast_indicated_day_ahead_history_publishtime_publishtime(publish_time, boundary=boundary, format=format)

Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatedForecastApi()
publish_time = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
boundary = 'boundary_example' # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
    api_response = api_instance.get_forecast_indicated_day_ahead_history_publishtime_publishtime(publish_time, boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatedForecastApi->get_forecast_indicated_day_ahead_history_publishtime_publishtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

