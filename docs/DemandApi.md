# elexonpy.DemandApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_demand**](DemandApi.md#get_demand) | **GET** /demand | This endpoint is obsolete, and this location may be removed with no further notice. 
[**get_demand_actual_total_from_from_to_to**](DemandApi.md#get_demand_actual_total_from_from_to_to) | **GET** /demand/actual/total | Actual total load (ATL/B0610)
[**get_demand_outturn**](DemandApi.md#get_demand_outturn) | **GET** /demand/outturn | Initial National Demand outturn (INDO)
[**get_demand_outturn_daily**](DemandApi.md#get_demand_outturn_daily) | **GET** /demand/outturn/daily | Initial National Demand outturn per day (INDOD)
[**get_demand_outturn_daily_stream**](DemandApi.md#get_demand_outturn_daily_stream) | **GET** /demand/outturn/daily/stream | Initial National Demand outturn per day (INDOD) stream
[**get_demand_outturn_stream**](DemandApi.md#get_demand_outturn_stream) | **GET** /demand/outturn/stream | Initial National Demand outturn (INDO) stream
[**get_demand_outturn_summary**](DemandApi.md#get_demand_outturn_summary) | **GET** /demand/outturn/summary | System demand summary (FUELINST)
[**get_demand_peak**](DemandApi.md#get_demand_peak) | **GET** /demand/peak | Peak demand per day (ITSDO)
[**get_demand_peak_indicative_data_data**](DemandApi.md#get_demand_peak_indicative_data_data) | **GET** /demand/peak/indicative | Indicative peak demand per day (S0142, ITSDO, FUELHH)
[**get_demand_peak_indicative_operational_triadseason**](DemandApi.md#get_demand_peak_indicative_operational_triadseason) | **GET** /demand/peak/indicative/operational/{triadSeason} | Operational data demand peaks for a Triad season (ITSDO, FUELHH)
[**get_demand_peak_indicative_settlement_triadseason**](DemandApi.md#get_demand_peak_indicative_settlement_triadseason) | **GET** /demand/peak/indicative/settlement/{triadSeason} | Settlement data demand peaks for a Triad season (S0142)
[**get_demand_peak_triad_data_data**](DemandApi.md#get_demand_peak_triad_data_data) | **GET** /demand/peak/triad | Triad demand peaks (S0142, ITSDO, FUELHH)
[**get_demand_rollingsystemdemand**](DemandApi.md#get_demand_rollingsystemdemand) | **GET** /demand/rollingSystemDemand | This endpoint is obsolete, and this location may be removed with no further notice. 
[**get_demand_stream**](DemandApi.md#get_demand_stream) | **GET** /demand/stream | This endpoint is obsolete, and this location may be removed with no further notice. 
[**get_demand_summary**](DemandApi.md#get_demand_summary) | **GET** /demand/summary | This endpoint is obsolete, and this location may be removed with no further notice. 
[**get_demand_total_actual**](DemandApi.md#get_demand_total_actual) | **GET** /demand/total/actual | This endpoint is obsolete, and this location may be removed with no further notice. 

# **get_demand**
> get_demand(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to demand/outturn.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.get_demand(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand: %s\n" % e)
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

# **get_demand_actual_total_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone get_demand_actual_total_from_from_to_to(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Actual total load (ATL/B0610)

This endpoint provides actual total load data per bidding zone.  It can be filtered by settlement period dates.                This API endpoint has a maximum range of 7 days.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
settlement_period_from = 56 # int | Format - int32. (optional)
settlement_period_to = 56 # int | Format - int32. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Actual total load (ATL/B0610)
    api_response = api_instance.get_demand_actual_total_from_from_to_to(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_actual_total_from_from_to_to: %s\n" % e)
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

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_outturn**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn get_demand_outturn(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, format=format)

Initial National Demand outturn (INDO)

This endpoint provides data for Initial National Demand Outturn, which measures the  half-hour average MW demand metered by the Transmission Company based on its operational metering.  The data is updated every 30 minutes and within 15 minutes of the end of the effective settlement period. The data is represented with:  - INDO (initial National Demand outturn) which takes into account transmission losses but does not include station transformer load, pumped storage demand or interconnector demand.  - ITSDO (initial Transmission System Demand outturn) which takes into account transmission losses, station transformer load, pumped storage demand and interconnector demand.                This endpoint is useful for ad-hoc querying of the data.                Settlement date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
settlement_date_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date from for the filter. This must be in the format yyyy-MM-dd. (optional)
settlement_date_to = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date to for the filter. This must be in the format yyyy-MM-dd. (optional)
settlement_period = [56] # list[int] |  (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Initial National Demand outturn (INDO)
    api_response = api_instance.get_demand_outturn(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_outturn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**| Format - date (as full-date in RFC3339). The settlement date from for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_date_to** | **date**| Format - date (as full-date in RFC3339). The settlement date to for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_period** | [**list[int]**](int.md)|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_outturn_daily**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow get_demand_outturn_daily(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, format=format)

Initial National Demand outturn per day (INDOD)

This endpoint provides initial National Demand outturn data per day. The total daily energy volume is the total  demand volume for the previous day expressed on an initial National Demand outturn (INDO) basis, i.e. excluding  station transformer, pumping and interconnector export demand. It is calculated from summing the half hourly  INDO demands (divided by two to convert to MWh).                If no date window is chosen, the search will default to results from the last 31 days.    This API endpoint has a maximum range of 2 years (731 days).

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
settlement_date_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). (optional)
settlement_date_to = '2013-10-20' # date | Format - date (as full-date in RFC3339). (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Initial National Demand outturn per day (INDOD)
    api_response = api_instance.get_demand_outturn_daily(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_outturn_daily: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**| Format - date (as full-date in RFC3339). | [optional] 
 **settlement_date_to** | **date**| Format - date (as full-date in RFC3339). | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_outturn_daily_stream**
> list[InsightsApiModelsResponsesDemandOutturnIndodRow] get_demand_outturn_daily_stream(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to)

Initial National Demand outturn per day (INDOD) stream

This endpoint provides initial National Demand outturn daily data. The total daily energy volume is the total  demand volume for the previous day expressed on an initial National Demand outturn (INDO) basis, i.e. excluding  station transformer, pumping and interconnector export demand. It is calculated from summing the half hourly  INDO demands (divided by two to convert to MWh).                If no date window is chosen, the search will default to results from the last 31 days.    This endpoint has an optimised JSON payload and is aimed at frequent requests for the data.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
settlement_date_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). (optional)
settlement_date_to = '2013-10-20' # date | Format - date (as full-date in RFC3339). (optional)

try:
    # Initial National Demand outturn per day (INDOD) stream
    api_response = api_instance.get_demand_outturn_daily_stream(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_outturn_daily_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**| Format - date (as full-date in RFC3339). | [optional] 
 **settlement_date_to** | **date**| Format - date (as full-date in RFC3339). | [optional] 

### Return type

[**list[InsightsApiModelsResponsesDemandOutturnIndodRow]**](InsightsApiModelsResponsesDemandOutturnIndodRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_outturn_stream**
> list[InsightsApiModelsResponsesDemandOutturnDemandOutturn] get_demand_outturn_stream(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period)

Initial National Demand outturn (INDO) stream

This endpoint provides data for initial National Demand outturn, which measures the  half-hour average MW demand metered by the Transmission Company based on its operational metering.  The data is updated every 30 minutes and within 15 minutes of the end of the effective settlement period. The data is represented with:  - INDO (initial National Demand outturn) which takes into account transmission losses but does not include station transformer load, pumped storage demand or interconnector demand.  - ITSDO (initial Transmission System Demand outturn) which takes into account transmission losses, station transformer load, pumped storage demand and interconnector demand.                This endpoint has an optimised JSON payload and is aimed at frequent requests for the data.                Settlement date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
settlement_date_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date from for the filter. This must be in the format yyyy-MM-dd. (optional)
settlement_date_to = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date to for the filter. This must be in the format yyyy-MM-dd. (optional)
settlement_period = [56] # list[int] |  (optional)

try:
    # Initial National Demand outturn (INDO) stream
    api_response = api_instance.get_demand_outturn_stream(settlement_date_from=settlement_date_from, settlement_date_to=settlement_date_to, settlement_period=settlement_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_outturn_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date_from** | **date**| Format - date (as full-date in RFC3339). The settlement date from for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_date_to** | **date**| Format - date (as full-date in RFC3339). The settlement date to for the filter. This must be in the format yyyy-MM-dd. | [optional] 
 **settlement_period** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**list[InsightsApiModelsResponsesDemandOutturnDemandOutturn]**](InsightsApiModelsResponsesDemandOutturnDemandOutturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_outturn_summary**
> list[InsightsApiModelsResponsesDemandOutturnRollingSystemDemand] get_demand_outturn_summary(resolution=resolution, _from=_from, to=to, format=format)

System demand summary (FUELINST)

⚠ This endpoint provides a down-sampled data summary intended for visualisation purposes.  Use datasets endpoints for full dataset access.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
resolution = 'resolution_example' # str |  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # System demand summary (FUELINST)
    api_response = api_instance.get_demand_outturn_summary(resolution=resolution, _from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_outturn_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution** | **str**|  | [optional] 
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**list[InsightsApiModelsResponsesDemandOutturnRollingSystemDemand]**](InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_peak**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak get_demand_peak(_from=_from, to=to, format=format)

Peak demand per day (ITSDO)

This endpoint allows for retrieving peak ITSDO demand for each day from National Grid ESO.  Results are filtered by a range of Date parameters.  Results default to yesterday's peak if no parameters are supplied.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). The start of the requested date range. (optional)
to = '2013-10-20' # date | Format - date (as full-date in RFC3339). The end of the requested date range. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Peak demand per day (ITSDO)
    api_response = api_instance.get_demand_peak(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_peak: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Format - date (as full-date in RFC3339). The start of the requested date range. | [optional] 
 **to** | **date**| Format - date (as full-date in RFC3339). The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_peak_indicative_data_data**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak get_demand_peak_indicative_data_data(data, triad_season_start_year=triad_season_start_year, _from=_from, to=to, format=format)

Indicative peak demand per day (S0142, ITSDO, FUELHH)

Indicative demand peaks using operational metering data are daily maxima values determined from  ITSDO and FUELHH data used to determine and visualise Triad.                Indicative demand peaks using settlement metering data are daily maxima values determined from  metered volume data from the S0142_bpi file. These peaks are not used for Triad visualisation as  they are always calculated based on the latest run type. Triads for settlement data  remain static after the National Grid report posted at the beginning of April after the Triad season has ended.                 If no filters are supplied, results default to the latest or current Triad season.  To specify a custom filter, you can supplier EITHER a Triad season start year, OR a date range, but not both.  If a Triad Season Start year is supplied, data for the Triad season beginning on 1 November  of the specified year will be returned.  If a date range is supplied, data will be returned for settlement dates within the date range inclusively.                Date parameters must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
data = 'data_example' # str | The type of data. Supports values of 'operational' or 'settlement'.
triad_season_start_year = 56 # int | Format - int32. A year indicating the Triad season starting on 1 November of the given year, e.g. 2021. (optional)
_from = '2013-10-20' # date | Format - date (as full-date in RFC3339). The start of the requested date range. (optional)
to = '2013-10-20' # date | Format - date (as full-date in RFC3339). The end of the requested date range. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Indicative peak demand per day (S0142, ITSDO, FUELHH)
    api_response = api_instance.get_demand_peak_indicative_data_data(data, triad_season_start_year=triad_season_start_year, _from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_peak_indicative_data_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| The type of data. Supports values of &#x27;operational&#x27; or &#x27;settlement&#x27;. | 
 **triad_season_start_year** | **int**| Format - int32. A year indicating the Triad season starting on 1 November of the given year, e.g. 2021. | [optional] 
 **_from** | **date**| Format - date (as full-date in RFC3339). The start of the requested date range. | [optional] 
 **to** | **date**| Format - date (as full-date in RFC3339). The end of the requested date range. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_peak_indicative_operational_triadseason**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak get_demand_peak_indicative_operational_triadseason(triad_season, format=format)

Operational data demand peaks for a Triad season (ITSDO, FUELHH)

Provides indicative demand peak data for a Triad season ITSDO and FUELHH files over a Triad season. For non-Triad  season dates please use the `peak/indicative` endpoint.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
triad_season = 56 # int | Format - int32. A year indicating the Triad season starting on 1 November of the given year
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Operational data demand peaks for a Triad season (ITSDO, FUELHH)
    api_response = api_instance.get_demand_peak_indicative_operational_triadseason(triad_season, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_peak_indicative_operational_triadseason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triad_season** | **int**| Format - int32. A year indicating the Triad season starting on 1 November of the given year | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_peak_indicative_settlement_triadseason**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak get_demand_peak_indicative_settlement_triadseason(triad_season, format=format)

Settlement data demand peaks for a Triad season (S0142)

Provides indicative demand peak data for a Triad season from S0142_bpi files that were calculated  during the Triad season. For the data from the latest settlement runs for the Triad season use the  `peak/indicative` endpoint.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
triad_season = 56 # int | Format - int32. A year indicating the Triad season starting on 1 November of the given year
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Settlement data demand peaks for a Triad season (S0142)
    api_response = api_instance.get_demand_peak_indicative_settlement_triadseason(triad_season, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_peak_indicative_settlement_triadseason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triad_season** | **int**| Format - int32. A year indicating the Triad season starting on 1 November of the given year | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_peak_triad_data_data**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak get_demand_peak_triad_data_data(data, triad_season_start_year=triad_season_start_year, format=format)

Triad demand peaks (S0142, ITSDO, FUELHH)

Operational Triad peaks are calculated from the indicative demand peaks data.    Settlement Triad Peaks are calculated from the latest metered volume data available at the point one month following the Triad season's end.  For any Triad season still in progress, the latest run type data is used.                All Triad peaks are at least 10 days clear of one another.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
data = 'data_example' # str | The type of data. Supports values of 'operational' or 'settlement'.
triad_season_start_year = 56 # int | Format - int32. A year indicating the Triad season starting on 1 November of the given year. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Triad demand peaks (S0142, ITSDO, FUELHH)
    api_response = api_instance.get_demand_peak_triad_data_data(data, triad_season_start_year=triad_season_start_year, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_peak_triad_data_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| The type of data. Supports values of &#x27;operational&#x27; or &#x27;settlement&#x27;. | 
 **triad_season_start_year** | **int**| Format - int32. A year indicating the Triad season starting on 1 November of the given year. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demand_rollingsystemdemand**
> get_demand_rollingsystemdemand(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to generation/outturn.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.get_demand_rollingsystemdemand(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_rollingsystemdemand: %s\n" % e)
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

# **get_demand_stream**
> get_demand_stream(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to demand/outturn/stream.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.get_demand_stream(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_stream: %s\n" % e)
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

# **get_demand_summary**
> get_demand_summary(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to demand/outturn/summary.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.get_demand_summary(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_summary: %s\n" % e)
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

# **get_demand_total_actual**
> get_demand_total_actual(format=format)

This endpoint is obsolete, and this location may be removed with no further notice. 

This endpoint has been moved to demand/actual/total.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.DemandApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. 
    api_instance.get_demand_total_actual(format=format)
except ApiException as e:
    print("Exception when calling DemandApi->get_demand_total_actual: %s\n" % e)
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

