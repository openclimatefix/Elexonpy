# swagger_client.DemandApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**demand_actual_total_get**](DemandApi.md#demand_actual_total_get) | **GET** /demand/actual/total | Actual total load (ATL/B0610)
[**demand_get**](DemandApi.md#demand_get) | **GET** /demand | This endpoint is obsolete, and this location may be removed with no further notice. 
[**demand_outturn_daily_get**](DemandApi.md#demand_outturn_daily_get) | **GET** /demand/outturn/daily | Initial National Demand outturn per day (INDOD)
[**demand_outturn_daily_stream_get**](DemandApi.md#demand_outturn_daily_stream_get) | **GET** /demand/outturn/daily/stream | Initial National Demand outturn per day (INDOD) stream
[**demand_outturn_get**](DemandApi.md#demand_outturn_get) | **GET** /demand/outturn | Initial National Demand outturn (INDO)
[**demand_outturn_stream_get**](DemandApi.md#demand_outturn_stream_get) | **GET** /demand/outturn/stream | Initial National Demand outturn (INDO) stream
[**demand_outturn_summary_get**](DemandApi.md#demand_outturn_summary_get) | **GET** /demand/outturn/summary | System demand summary (FUELINST)
[**demand_peak_get**](DemandApi.md#demand_peak_get) | **GET** /demand/peak | Peak demand per day (ITSDO)
[**demand_peak_indicative_get**](DemandApi.md#demand_peak_indicative_get) | **GET** /demand/peak/indicative | Indicative peak demand per day (S0142, ITSDO, FUELHH)
[**demand_peak_indicative_operational_triad_season_get**](DemandApi.md#demand_peak_indicative_operational_triad_season_get) | **GET** /demand/peak/indicative/operational/{triadSeason} | Operational data demand peaks for a Triad season (ITSDO, FUELHH)
[**demand_peak_indicative_settlement_triad_season_get**](DemandApi.md#demand_peak_indicative_settlement_triad_season_get) | **GET** /demand/peak/indicative/settlement/{triadSeason} | Settlement data demand peaks for a Triad season (S0142)
[**demand_peak_triad_get**](DemandApi.md#demand_peak_triad_get) | **GET** /demand/peak/triad | Triad demand peaks (S0142, ITSDO, FUELHH)
[**demand_rolling_system_demand_get**](DemandApi.md#demand_rolling_system_demand_get) | **GET** /demand/rollingSystemDemand | This endpoint is obsolete, and this location may be removed with no further notice. 
[**demand_stream_get**](DemandApi.md#demand_stream_get) | **GET** /demand/stream | This endpoint is obsolete, and this location may be removed with no further notice. 
[**demand_summary_get**](DemandApi.md#demand_summary_get) | **GET** /demand/summary | This endpoint is obsolete, and this location may be removed with no further notice. 
[**demand_total_actual_get**](DemandApi.md#demand_total_actual_get) | **GET** /demand/total/actual | This endpoint is obsolete, and this location may be removed with no further notice. 

# **demand_actual_total_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone demand_actual_total_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Actual total load (ATL/B0610)

This endpoint provides actual total load data per bidding zone.  It can be filtered by settlement period dates.                This API endpoint has a maximum range of 7 days.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | 
to = '2013-10-20T19:20:30+01:00' # datetime | 
settlement_period_from = 56 # int |  (optional)
settlement_period_to = 56 # int |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Actual total load (ATL/B0610)
    api_response = api_instance.demand_actual_total_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_actual_total_get: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_get**
> demand_get(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to demand/outturn.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.demand_get(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->demand_get: %s\n" % e)
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

# **demand_outturn_daily_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow demand_outturn_daily_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, format=format)

Initial National Demand outturn per day (INDOD)

This endpoint provides initial National Demand outturn data per day. The total daily energy volume is the total  demand volume for the previous day expressed on an initial National Demand outturn (INDO) basis, i.e. excluding  station transformer, pumping and interconnector export demand. It is calculated from summing the half hourly  INDO demands (divided by two to convert to MWh).                If no date window is chosen, the search will default to results from the last 31 days.    This API endpoint has a maximum range of 2 years (731 days).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
settlement_date_from = '2013-10-20' # date |  (optional)
settlement_date_to = '2013-10-20' # date |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Initial National Demand outturn per day (INDOD)
    api_response = api_instance.demand_outturn_daily_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_outturn_daily_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**|  | [optional] 
 **settlement_date_to** | **date**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_outturn_daily_stream_get**
> list[InsightsApiModelsResponsesDemandOutturnIndodRow] demand_outturn_daily_stream_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to)

Initial National Demand outturn per day (INDOD) stream

This endpoint provides initial National Demand outturn daily data. The total daily energy volume is the total  demand volume for the previous day expressed on an initial National Demand outturn (INDO) basis, i.e. excluding  station transformer, pumping and interconnector export demand. It is calculated from summing the half hourly  INDO demands (divided by two to convert to MWh).                If no date window is chosen, the search will default to results from the last 31 days.    This endpoint has an optimised JSON payload and is aimed at frequent requests for the data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
settlement_date_from = '2013-10-20' # date |  (optional)
settlement_date_to = '2013-10-20' # date |  (optional)

try:
    # Initial National Demand outturn per day (INDOD) stream
    api_response = api_instance.demand_outturn_daily_stream_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_outturn_daily_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**|  | [optional] 
 **settlement_date_to** | **date**|  | [optional] 

### Return type

[**list[InsightsApiModelsResponsesDemandOutturnIndodRow]**](InsightsApiModelsResponsesDemandOutturnIndodRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_outturn_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn demand_outturn_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, format=format)

Initial National Demand outturn (INDO)

This endpoint provides data for Initial National Demand Outturn, which measures the  half-hour average MW demand metered by the Transmission Company based on its operational metering.  The data is updated every 30 minutes and within 15 minutes of the end of the effective settlement period. The data is represented with:  - INDO (initial National Demand outturn) which takes into account transmission losses but does not include station transformer load, pumped storage demand or interconnector demand.  - ITSDO (initial Transmission System Demand outturn) which takes into account transmission losses, station transformer load, pumped storage demand and interconnector demand.                This endpoint is useful for ad-hoc querying of the data.                Settlement date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
settlement_date_from = '2013-10-20' # date | The settlement date from for the filter. This must be in the format yyyy-MM-dd. (optional)
settlement_date_to = '2013-10-20' # date | The settlement date to for the filter. This must be in the format yyyy-MM-dd. (optional)
settlement_period = [56] # list[int] |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Initial National Demand outturn (INDO)
    api_response = api_instance.demand_outturn_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_outturn_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**| The settlement date from for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_date_to** | **date**| The settlement date to for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_period** | [**list[int]**](int.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_outturn_stream_get**
> list[InsightsApiModelsResponsesDemandOutturnDemandOutturn] demand_outturn_stream_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period)

Initial National Demand outturn (INDO) stream

This endpoint provides data for initial National Demand outturn, which measures the  half-hour average MW demand metered by the Transmission Company based on its operational metering.  The data is updated every 30 minutes and within 15 minutes of the end of the effective settlement period. The data is represented with:  - INDO (initial National Demand outturn) which takes into account transmission losses but does not include station transformer load, pumped storage demand or interconnector demand.  - ITSDO (initial Transmission System Demand outturn) which takes into account transmission losses, station transformer load, pumped storage demand and interconnector demand.                This endpoint has an optimised JSON payload and is aimed at frequent requests for the data.                Settlement date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
settlement_date_from = '2013-10-20' # date | The settlement date from for the filter. This must be in the format yyyy-MM-dd. (optional)
settlement_date_to = '2013-10-20' # date | The settlement date to for the filter. This must be in the format yyyy-MM-dd. (optional)
settlement_period = [56] # list[int] |  (optional)

try:
    # Initial National Demand outturn (INDO) stream
    api_response = api_instance.demand_outturn_stream_get(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_outturn_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**| The settlement date from for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_date_to** | **date**| The settlement date to for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_period** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**list[InsightsApiModelsResponsesDemandOutturnDemandOutturn]**](InsightsApiModelsResponsesDemandOutturnDemandOutturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_outturn_summary_get**
> list[InsightsApiModelsResponsesDemandOutturnRollingSystemDemand] demand_outturn_summary_get(_from=_from, to=to, format=format)

System demand summary (FUELINST)

⚠ This endpoint provides a down-sampled data summary intended for visualisation purposes.  Use datasets endpoints for full dataset access.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # System demand summary (FUELINST)
    api_response = api_instance.demand_outturn_summary_get(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_outturn_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**list[InsightsApiModelsResponsesDemandOutturnRollingSystemDemand]**](InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_peak_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak demand_peak_get(_from=_from, to=to, format=format)

Peak demand per day (ITSDO)

This endpoint allows for retrieving peak ITSDO demand for each day from National Grid ESO.  Results are filtered by a range of Date parameters.  Results default to yesterday's peak if no parameters are supplied.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
_from = '2013-10-20' # date | The start of the requested date range. (optional)
to = '2013-10-20' # date | The end of the requested date range. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Peak demand per day (ITSDO)
    api_response = api_instance.demand_peak_get(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_peak_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| The start of the requested date range. | [optional] 
 **to** | **date**| The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_peak_indicative_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak demand_peak_indicative_get(data, triad_season_start_year=triad_season_start_year, _from=_from, to=to, format=format)

Indicative peak demand per day (S0142, ITSDO, FUELHH)

Indicative demand peaks using operational metering data are daily maxima values determined from  ITSDO and FUELHH data used to determine and visualise Triad.                Indicative demand peaks using settlement metering data are daily maxima values determined from  metered volume data from the S0142_bpi file. These peaks are not used for Triad visualisation as  they are always calculated based on the latest run type. Triads for settlement data  remain static after the National Grid report posted at the beginning of April after the Triad season has ended.                 If no filters are supplied, results default to the latest or current Triad season.  To specify a custom filter, you can supplier EITHER a Triad season start year, OR a date range, but not both.  If a Triad Season Start year is supplied, data for the Triad season beginning on 1 November  of the specified year will be returned.  If a date range is supplied, data will be returned for settlement dates within the date range inclusively.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
data = 'data_example' # str | The type of data. Supports values of 'operational' or 'settlement'.
triad_season_start_year = 56 # int | A year indicating the Triad season starting on 1 November of the given year, e.g. 2021. (optional)
_from = '2013-10-20' # date | The start of the requested date range. (optional)
to = '2013-10-20' # date | The end of the requested date range. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Indicative peak demand per day (S0142, ITSDO, FUELHH)
    api_response = api_instance.demand_peak_indicative_get(data, triad_season_start_year=triad_season_start_year, _from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_peak_indicative_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| The type of data. Supports values of &#x27;operational&#x27; or &#x27;settlement&#x27;. | 
 **triad_season_start_year** | **int**| A year indicating the Triad season starting on 1 November of the given year, e.g. 2021. | [optional] 
 **_from** | **date**| The start of the requested date range. | [optional] 
 **to** | **date**| The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_peak_indicative_operational_triad_season_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak demand_peak_indicative_operational_triad_season_get(triad_season, format=format)

Operational data demand peaks for a Triad season (ITSDO, FUELHH)

Provides indicative demand peak data for a Triad season ITSDO and FUELHH files over a Triad season. For non-Triad  season dates please use the `peak/indicative` endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
triad_season = 56 # int | A year indicating the Triad season starting on 1 November of the given year
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Operational data demand peaks for a Triad season (ITSDO, FUELHH)
    api_response = api_instance.demand_peak_indicative_operational_triad_season_get(triad_season, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_peak_indicative_operational_triad_season_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triad_season** | **int**| A year indicating the Triad season starting on 1 November of the given year | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_peak_indicative_settlement_triad_season_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak demand_peak_indicative_settlement_triad_season_get(triad_season, format=format)

Settlement data demand peaks for a Triad season (S0142)

Provides indicative demand peak data for a Triad season from S0142_bpi files that were calculated  during the Triad season. For the data from the latest settlement runs for the Triad season use the  `peak/indicative` endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
triad_season = 56 # int | A year indicating the Triad season starting on 1 November of the given year
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Settlement data demand peaks for a Triad season (S0142)
    api_response = api_instance.demand_peak_indicative_settlement_triad_season_get(triad_season, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_peak_indicative_settlement_triad_season_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triad_season** | **int**| A year indicating the Triad season starting on 1 November of the given year | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_peak_triad_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak demand_peak_triad_get(data, triad_season_start_year=triad_season_start_year, format=format)

Triad demand peaks (S0142, ITSDO, FUELHH)

Operational Triad peaks are calculated from the indicative demand peaks data.    Settlement Triad Peaks are calculated from the latest metered volume data available at the point one month following the Triad season's end.  For any Triad season still in progress, the latest run type data is used.                All Triad peaks are at least 10 days clear of one another.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
data = 'data_example' # str | The type of data. Supports values of 'operational' or 'settlement'.
triad_season_start_year = 56 # int | A year indicating the Triad season starting on 1 November of the given year. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Triad demand peaks (S0142, ITSDO, FUELHH)
    api_response = api_instance.demand_peak_triad_get(data, triad_season_start_year=triad_season_start_year, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->demand_peak_triad_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| The type of data. Supports values of &#x27;operational&#x27; or &#x27;settlement&#x27;. | 
 **triad_season_start_year** | **int**| A year indicating the Triad season starting on 1 November of the given year. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demand_rolling_system_demand_get**
> demand_rolling_system_demand_get(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to generation/outturn.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.demand_rolling_system_demand_get(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->demand_rolling_system_demand_get: %s\n" % e)
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

# **demand_stream_get**
> demand_stream_get(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to demand/outturn/stream.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.demand_stream_get(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->demand_stream_get: %s\n" % e)
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

# **demand_summary_get**
> demand_summary_get(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to demand/outturn/summary.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.demand_summary_get(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->demand_summary_get: %s\n" % e)
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

# **demand_total_actual_get**
> demand_total_actual_get(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to demand/actual/total.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.demand_total_actual_get(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->demand_total_actual_get: %s\n" % e)
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

