# swagger_client.IndicatedForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_indicated_day_ahead_evolution_get**](IndicatedForecastApi.md#forecast_indicated_day_ahead_evolution_get) | **GET** /forecast/indicated/day-ahead/evolution | Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
[**forecast_indicated_day_ahead_get**](IndicatedForecastApi.md#forecast_indicated_day_ahead_get) | **GET** /forecast/indicated/day-ahead | Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
[**forecast_indicated_day_ahead_history_get**](IndicatedForecastApi.md#forecast_indicated_day_ahead_history_get) | **GET** /forecast/indicated/day-ahead/history | Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)

# **forecast_indicated_day_ahead_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast forecast_indicated_day_ahead_evolution_get(settlement_date, settlement_period, boundary=boundary, format=format)

Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)

This endpoint provides the forecast indicated day-ahead data over time for the specified settlement date and settlement period.    Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicatedForecastApi()
settlement_date = '2013-10-20'  # date | The settlement date for the filter. This must be in the format yyyy-MM-dd.
settlement_period = [56]  # list[int] | 
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
    api_response = api_instance.forecast_indicated_day_ahead_evolution_get(settlement_date, settlement_period,
                                                                           boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatedForecastApi->forecast_indicated_day_ahead_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **settlement_period** | [**list[int]**](int.md)|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_indicated_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast forecast_indicated_day_ahead_get(boundary=boundary, format=format)

Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)

This endpoint provides the latest forecast indicated day-ahead data

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicatedForecastApi()
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
    api_response = api_instance.forecast_indicated_day_ahead_get(boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatedForecastApi->forecast_indicated_day_ahead_get: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_indicated_day_ahead_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast forecast_indicated_day_ahead_history_get(publish_time, boundary=boundary, format=format)

Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicatedForecastApi()
publish_time = '2013-10-20T19:20:30+01:00'  # datetime | 
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
    api_response = api_instance.forecast_indicated_day_ahead_history_get(publish_time, boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatedForecastApi->forecast_indicated_day_ahead_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

