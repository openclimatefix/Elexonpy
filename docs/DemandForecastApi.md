# swagger_client.DemandForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_demand_daily_evolution_get**](DemandForecastApi.md#forecast_demand_daily_evolution_get) | **GET** /forecast/demand/daily/evolution | Evolution of the fourteen-day demand forecast over time (NDFD, TSDFD)
[**forecast_demand_daily_get**](DemandForecastApi.md#forecast_demand_daily_get) | **GET** /forecast/demand/daily | Fourteen day demand forecast (NDFD, TSDFD)
[**forecast_demand_daily_history_get**](DemandForecastApi.md#forecast_demand_daily_history_get) | **GET** /forecast/demand/daily/history | History of the fourteen-day demand forecast (NDFD, TSDFD)
[**forecast_demand_day_ahead_earliest_get**](DemandForecastApi.md#forecast_demand_day_ahead_earliest_get) | **GET** /forecast/demand/day-ahead/earliest | Historic view of the earliest forecasted demand (NDF, TSDF)
[**forecast_demand_day_ahead_earliest_stream_get**](DemandForecastApi.md#forecast_demand_day_ahead_earliest_stream_get) | **GET** /forecast/demand/day-ahead/earliest/stream | Historic view of the earliest forecasted demand (NDF, TSDF) stream
[**forecast_demand_day_ahead_evolution_get**](DemandForecastApi.md#forecast_demand_day_ahead_evolution_get) | **GET** /forecast/demand/day-ahead/evolution | Evolution of the day-ahead demand forecast over time (NDF, TSDF)
[**forecast_demand_day_ahead_get**](DemandForecastApi.md#forecast_demand_day_ahead_get) | **GET** /forecast/demand/day-ahead | Day-ahead demand forecast (NDF, TSDF)
[**forecast_demand_day_ahead_history_get**](DemandForecastApi.md#forecast_demand_day_ahead_history_get) | **GET** /forecast/demand/day-ahead/history | History of the day-ahead demand forecast (NDF, TSDF)
[**forecast_demand_day_ahead_latest_get**](DemandForecastApi.md#forecast_demand_day_ahead_latest_get) | **GET** /forecast/demand/day-ahead/latest | Historic view of the latest forecasted demand (NDF, TSDF)
[**forecast_demand_day_ahead_latest_stream_get**](DemandForecastApi.md#forecast_demand_day_ahead_latest_stream_get) | **GET** /forecast/demand/day-ahead/latest/stream | Historic view of the latest forecasted demand (NDF, TSDF) stream
[**forecast_demand_day_ahead_peak_get**](DemandForecastApi.md#forecast_demand_day_ahead_peak_get) | **GET** /forecast/demand/day-ahead/peak | Peak forecasted demand per day (TSDF)
[**forecast_demand_total_day_ahead_get**](DemandForecastApi.md#forecast_demand_total_day_ahead_get) | **GET** /forecast/demand/total/day-ahead | Day-ahead total load forecast (DATL/B0620)
[**forecast_demand_total_week_ahead_get**](DemandForecastApi.md#forecast_demand_total_week_ahead_get) | **GET** /forecast/demand/total/week-ahead | Week-ahead total load forecast (WATL/B0630)
[**forecast_demand_total_week_ahead_latest_get**](DemandForecastApi.md#forecast_demand_total_week_ahead_latest_get) | **GET** /forecast/demand/total/week-ahead/latest | Latest week-ahead total load forecast (WATL/B0630)
[**forecast_demand_weekly_evolution_get**](DemandForecastApi.md#forecast_demand_weekly_evolution_get) | **GET** /forecast/demand/weekly/evolution | Evolution of the one-year demand forecast over time  (NDFW, TSDFW)
[**forecast_demand_weekly_get**](DemandForecastApi.md#forecast_demand_weekly_get) | **GET** /forecast/demand/weekly | One-year demand forecast (NDFW, TSDFW)
[**forecast_demand_weekly_history_get**](DemandForecastApi.md#forecast_demand_weekly_history_get) | **GET** /forecast/demand/weekly/history | History of the one-year demand forecast (NDFW, TSDFW)

# **forecast_demand_daily_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily forecast_demand_daily_evolution_get(forecast_date, format=format)

Evolution of the fourteen-day demand forecast over time (NDFD, TSDFD)

This endpoint provides the evolution of all daily demand forecasts over time for a given forecast date.                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
forecast_date = '2013-10-20'  # date | The forecast date for the filter. This must be in the format yyyy-MM-dd.
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the fourteen-day demand forecast over time (NDFD, TSDFD)
    api_response = api_instance.forecast_demand_daily_evolution_get(forecast_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_daily_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_date** | **date**| The forecast date for the filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily forecast_demand_daily_get(format=format)

Fourteen day demand forecast (NDFD, TSDFD)

Retrieve latest 14-day forecast demand data

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Fourteen day demand forecast (NDFD, TSDFD)
    api_response = api_instance.forecast_demand_daily_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_daily_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_daily_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily forecast_demand_daily_history_get(publish_time, format=format)

History of the fourteen-day demand forecast (NDFD, TSDFD)

Retrieve historical daily forecast demand data

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
publish_time = '2013-10-20T19:20:30+01:00'  # datetime | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the fourteen-day demand forecast (NDFD, TSDFD)
    api_response = api_instance.forecast_demand_daily_history_get(publish_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_daily_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_earliest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_earliest_get(_from, to, boundary=boundary, format=format)

Historic view of the earliest forecasted demand (NDF, TSDF)

This endpoint allows for retrieving earliest day-ahead demand forecast data from National Grid ESO.  Results are filtered by settlement time, and only the earliest published forecast for each settlement period is shown.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic view of the earliest forecasted demand (NDF, TSDF)
    api_response = api_instance.forecast_demand_day_ahead_earliest_get(_from, to, boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_earliest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_earliest_stream_get**
> list[InsightsApiModelsServiceDayAheadDemandForecastRow] forecast_demand_day_ahead_earliest_stream_get(_from, to, boundary=boundary)

Historic view of the earliest forecasted demand (NDF, TSDF) stream

This endpoint allows for retrieving a stream of earliest day-ahead demand forecast data from National Grid ESO.  Results are filtered by settlement time, and only the earliest published forecast for each settlement period is shown.  This endpoint has an optimised JSON payload and aimed at frequent request for the day-ahead demand forecast data.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)

try:
    # Historic view of the earliest forecasted demand (NDF, TSDF) stream
    api_response = api_instance.forecast_demand_day_ahead_earliest_stream_get(_from, to, boundary=boundary)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_earliest_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 

### Return type

[**list[InsightsApiModelsServiceDayAheadDemandForecastRow]**](InsightsApiModelsServiceDayAheadDemandForecastRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_evolution_get(settlement_date, settlement_period, boundary=boundary, format=format)

Evolution of the day-ahead demand forecast over time (NDF, TSDF)

This endpoint provides the day and day ahead demand forecast and are categorized as National Demand Forecast (NDF) and Transmission System Demand Forecast (TSDF);  the forecast values are derived by NGESO and is based on historically metered generation output for Great Britain.  The data is updated every 30 minutes and within 15 minutes of the end of the effective Settlement Period.  NDF takes into account transmission losses but but does not include station transformer load, pumped storage demand or Interconnector demand;  the data is reported only at national level; and TSDF which takes into account transmission losses , station transformer load, pumped storage demand and interconnector demand.  The data is reported both at national and boundary (system zones) level. Boundary data only available for Transmission System Demand Forecast (TSDF).                Date parameter must be provided in the exact format yyyy-MM-dd.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
settlement_date = '2013-10-20'  # date | The settlement date for the filter. This must be in the format yyyy-MM-dd.
settlement_period = [56]  # list[int] | 
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the day-ahead demand forecast over time (NDF, TSDF)
    api_response = api_instance.forecast_demand_day_ahead_evolution_get(settlement_date, settlement_period,
                                                                        boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **settlement_period** | [**list[int]**](int.md)|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_get(boundary=boundary, format=format)

Day-ahead demand forecast (NDF, TSDF)

This endpoint provides the day and day ahead demand forecast and are categorized as National Demand Forecast (NDF) and Transmission System Demand Forecast (TSDF);  the forecast values are derived by NGESO and is based on historically metered generation output for Great Britain.  The data is updated every 30 minutes and within 15 minutes of the end of the effective Settlement Period.  NDF takes into account transmission losses but but does not include station transformer load, pumped storage demand or Interconnector demand;  the data is reported only at national level; and TSDF which takes into account transmission losses , station transformer load, pumped storage demand and interconnector demand.  The data is reported both at national and boundary (system zones) level. Boundary data only available for Transmission System Demand Forecast (TSDF).

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Day-ahead demand forecast (NDF, TSDF)
    api_response = api_instance.forecast_demand_day_ahead_get(boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_history_get(publish_time, boundary=boundary, format=format)

History of the day-ahead demand forecast (NDF, TSDF)

This endpoint provides the day and day ahead demand forecast and are categorized as National Demand Forecast (NDF) and Transmission System Demand Forecast (TSDF);  the forecast values are derived by NGESO and is based on historically metered generation output for Great Britain.  The data is updated every 30 minutes and within 15 minutes of the end of the effective Settlement Period.  NDF takes into account transmission losses but but does not include station transformer load, pumped storage demand or Interconnector demand;  the data is reported only at national level; and TSDF which takes into account transmission losses , station transformer load, pumped storage demand and interconnector demand.  The data is reported both at national and boundary (system zones) level. Boundary data only available for Transmission System Demand Forecast (TSDF).

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
publish_time = '2013-10-20T19:20:30+01:00'  # datetime | 
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the day-ahead demand forecast (NDF, TSDF)
    api_response = api_instance.forecast_demand_day_ahead_history_get(publish_time, boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_latest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead forecast_demand_day_ahead_latest_get(_from, to, boundary=boundary, format=format)

Historic view of the latest forecasted demand (NDF, TSDF)

This endpoint allows for retrieving latest day-ahead demand forecast data from National Grid ESO.  Results are filtered by settlement time, and only the latest published forecast for each settlement period is shown.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic view of the latest forecasted demand (NDF, TSDF)
    api_response = api_instance.forecast_demand_day_ahead_latest_get(_from, to, boundary=boundary, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_latest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_latest_stream_get**
> list[InsightsApiModelsServiceDayAheadDemandForecastRow] forecast_demand_day_ahead_latest_stream_get(_from, to, boundary=boundary)

Historic view of the latest forecasted demand (NDF, TSDF) stream

This endpoint allows for retrieving a stream of latest day-ahead demand forecast data from National Grid ESO.  Results are filtered by settlement time, and only the latest published forecast for each settlement period is shown.  This endpoint has an optimised JSON payload and aimed at frequent request for the day-ahead demand forecast data.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
boundary = 'boundary_example'  # str | Omitting this will return only national data. Specifying boundary=zonal will return only zonal data. (optional)

try:
    # Historic view of the latest forecasted demand (NDF, TSDF) stream
    api_response = api_instance.forecast_demand_day_ahead_latest_stream_get(_from, to, boundary=boundary)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_latest_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **boundary** | **str**| Omitting this will return only national data. Specifying boundary&#x3D;zonal will return only zonal data. | [optional] 

### Return type

[**list[InsightsApiModelsServiceDayAheadDemandForecastRow]**](InsightsApiModelsServiceDayAheadDemandForecastRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_day_ahead_peak_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak forecast_demand_day_ahead_peak_get(boundary=boundary, _from=_from, to=to, format=format)

Peak forecasted demand per day (TSDF)

This endpoint allows for retrieving the peak demand that is forecast for each day from National Grid ESO.  Results are filtered by a range of Date parameters.  Results default to yesterday, today and tomorrow if no parameters are supplied.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
boundary = 'boundary_example'  # str |  (optional)
_from = '2013-10-20'  # date | The start of the requested date range. (optional)
to = '2013-10-20'  # date | The end of the requested date range. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Peak forecasted demand per day (TSDF)
    api_response = api_instance.forecast_demand_day_ahead_peak_get(boundary=boundary, _from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_day_ahead_peak_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary** | **str**|  | [optional] 
 **_from** | **date**| The start of the requested date range. | [optional] 
 **to** | **date**| The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_total_day_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone forecast_demand_total_day_ahead_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Day-ahead total load forecast (DATL/B0620)

This endpoint provides day-ahead total load forecast per bidding zone data.  It can be filtered by settlement period dates.                This API endpoint has a maximum range of 7 days.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
settlement_period_from = 56  # int |  (optional)
settlement_period_to = 56  # int |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Day-ahead total load forecast (DATL/B0620)
    api_response = api_instance.forecast_demand_total_day_ahead_get(_from, to,
                                                                    settlement_period_from=settlement_period_from,
                                                                    settlement_period_to=settlement_period_to,
                                                                    format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_total_day_ahead_get: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_total_week_ahead_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone forecast_demand_total_week_ahead_get(_from, to, format=format)

Week-ahead total load forecast (WATL/B0630)

This endpoint returns week-ahead total load forecast per bidding zone data with the minimum possible  and maximum available total loads in MW values, filtered by forecast week.                For a given forecast date, if more than one forecast has been published, only the most recent forecast  is returned.                This API endpoint has a maximum range of 367 days.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
_from = '2013-10-20'  # date | The earliest forecast date to include.
to = '2013-10-20'  # date | The latest forecast date to include.
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Week-ahead total load forecast (WATL/B0630)
    api_response = api_instance.forecast_demand_total_week_ahead_get(_from, to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_total_week_ahead_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| The earliest forecast date to include. | 
 **to** | **date**| The latest forecast date to include. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_total_week_ahead_latest_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone forecast_demand_total_week_ahead_latest_get(format=format)

Latest week-ahead total load forecast (WATL/B0630)

This endpoint returns the most recently published WATL / B0630 forecast.                This forecast is the week-ahead total load forecast per bidding zone data,  with minimum possible and maximum available total loads in MW values.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Latest week-ahead total load forecast (WATL/B0630)
    api_response = api_instance.forecast_demand_total_week_ahead_latest_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_total_week_ahead_latest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_weekly_evolution_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly forecast_demand_weekly_evolution_get(forecast_year, forecast_week, format=format)

Evolution of the one-year demand forecast over time  (NDFW, TSDFW)

This endpoint provides all weekly demand forecasts over time for a given forecast Year and Week

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
forecast_year = 56  # int | 
forecast_week = 56  # int | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Evolution of the one-year demand forecast over time  (NDFW, TSDFW)
    api_response = api_instance.forecast_demand_weekly_evolution_get(forecast_year, forecast_week, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_weekly_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forecast_year** | **int**|  | 
 **forecast_week** | **int**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_weekly_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly forecast_demand_weekly_get(format=format)

One-year demand forecast (NDFW, TSDFW)

This endpoint provides the latest weekly forecast demand data

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # One-year demand forecast (NDFW, TSDFW)
    api_response = api_instance.forecast_demand_weekly_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_weekly_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_demand_weekly_history_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly forecast_demand_weekly_history_get(publish_time, format=format)

History of the one-year demand forecast (NDFW, TSDFW)

Retrieve historical weekly forecast demand data

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandForecastApi()
publish_time = '2013-10-20T19:20:30+01:00'  # datetime | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # History of the one-year demand forecast (NDFW, TSDFW)
    api_response = api_instance.forecast_demand_weekly_history_get(publish_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandForecastApi->forecast_demand_weekly_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_time** | **datetime**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

