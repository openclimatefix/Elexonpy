# elexonpy.IndicativeImbalanceSettlementApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate) | **GET** /balancing/settlement/acceptance/volumes/all/{bidOffer}/{settlementDate} | Acceptance volumes by settlement date (BOAV)
[**get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate_sett**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate_sett) | **GET** /balancing/settlement/acceptance/volumes/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Acceptance volumes by settlement period (BOAV)
[**get_balancing_settlement_acceptances_all_settlementdate_settlementperiod**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_acceptances_all_settlementdate_settlementperiod) | **GET** /balancing/settlement/acceptances/all/{settlementDate}/{settlementPeriod} | Historic acceptances by settlement period (ISPSTACK, BOALF, BOD)
[**get_balancing_settlement_default_notices**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_default_notices) | **GET** /balancing/settlement/default-notices | Default notices (CDN)
[**get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate) | **GET** /balancing/settlement/indicative/cashflows/all/{bidOffer}/{settlementDate} | Indicative period BMU cashflows by settlement date (EBOCF)
[**get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate_se**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate_se) | **GET** /balancing/settlement/indicative/cashflows/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Indicative period BMU cashflows by settlement period (EBOCF)
[**get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate) | **GET** /balancing/settlement/indicative/volumes/all/{bidOffer}/{settlementDate} | Indicative volumes by settlement date (DISPTAV)
[**get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate_sett**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate_sett) | **GET** /balancing/settlement/indicative/volumes/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Indicative volumes by settlement period (DISPTAV)
[**get_balancing_settlement_market_depth_settlementdate**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_market_depth_settlementdate) | **GET** /balancing/settlement/market-depth/{settlementDate} | Market depth by settlement date (IMBALNGC, BOD, DISEBSP, DISPTAV)
[**get_balancing_settlement_market_depth_settlementdate_settlementperiod**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_market_depth_settlementdate_settlementperiod) | **GET** /balancing/settlement/market-depth/{settlementDate}/{settlementPeriod} | Market depth by settlement period (IMBALNGC, BOD, DISEBSP, DISPTAV)
[**get_balancing_settlement_messages_settlementdate**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_messages_settlementdate) | **GET** /balancing/settlement/messages/{settlementDate} | Settlement messages by settlement date (SMSG)
[**get_balancing_settlement_messages_settlementdate_settlementperiod**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_messages_settlementdate_settlementperiod) | **GET** /balancing/settlement/messages/{settlementDate}/{settlementPeriod} | Settlement messages by settlement date and period (SMSG)
[**get_balancing_settlement_stack_all_bidoffer_settlementdate_settlementperiod**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_stack_all_bidoffer_settlementdate_settlementperiod) | **GET** /balancing/settlement/stack/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Settlement bid-offer stacks by settlement period (ISPSTACK)
[**get_balancing_settlement_summary_settlementdate_settlementperiod**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_summary_settlementdate_settlementperiod) | **GET** /balancing/settlement/summary/{settlementDate}/{settlementPeriod} | Settlement calculation summary (ISPSTACK, DISEBSP, MID, NETBSAD)
[**get_balancing_settlement_system_prices_settlementdate**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_system_prices_settlementdate) | **GET** /balancing/settlement/system-prices/{settlementDate} | Settlement system prices by settlement date (DISEBSP)
[**get_balancing_settlement_system_prices_settlementdate_settlementperiod**](IndicativeImbalanceSettlementApi.md#get_balancing_settlement_system_prices_settlementdate_settlementperiod) | **GET** /balancing/settlement/system-prices/{settlementDate}/{settlementPeriod} | Settlement system prices by settlement date and period (DISEBSP)

# **get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate(settlement_date, bid_offer, bm_unit=bm_unit, format=format)

Acceptance volumes by settlement date (BOAV)

Returns the settlement acceptance volumes for the requested settlement date.    For each settlement period within the range, only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd.
bid_offer = 'bid_offer_example' # str | 
bm_unit = ['bm_unit_example'] # list[str] | Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Acceptance volumes by settlement date (BOAV)
    api_response = api_instance.get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate(settlement_date, bid_offer, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd. | 
 **bid_offer** | **str**|  | 
 **bm_unit** | [**list[str]**](str.md)| Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate_sett**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate_sett(settlement_period, settlement_date, bid_offer, bm_unit=bm_unit, format=format)

Acceptance volumes by settlement period (BOAV)

Returns the settlement acceptance volumes for the requested settlement period.    Only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_period = 56 # int | Format - int32. This should be an integer from 1-50 inclusive.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd.
bid_offer = 'bid_offer_example' # str | 
bm_unit = ['bm_unit_example'] # list[str] | Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Acceptance volumes by settlement period (BOAV)
    api_response = api_instance.get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate_sett(settlement_period, settlement_date, bid_offer, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_acceptance_volumes_all_bidoffer_settlementdate_sett: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_period** | **int**| Format - int32. This should be an integer from 1-50 inclusive. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd. | 
 **bid_offer** | **str**|  | 
 **bm_unit** | [**list[str]**](str.md)| Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_acceptances_all_settlementdate_settlementperiod**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse get_balancing_settlement_acceptances_all_settlementdate_settlementperiod(settlement_date, settlement_period, format=format)

Historic acceptances by settlement period (ISPSTACK, BOALF, BOD)

Returns the bid and offer prices for acceptances, with the acceptance number and acceptance time. Results are sorted by descending acceptance time.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd.
settlement_period = 56 # int | Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Historic acceptances by settlement period (ISPSTACK, BOALF, BOD)
    api_response = api_instance.get_balancing_settlement_acceptances_all_settlementdate_settlementperiod(settlement_date, settlement_period, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_acceptances_all_settlementdate_settlementperiod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **settlement_period** | **int**| Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_default_notices**
> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse get_balancing_settlement_default_notices(format=format)

Default notices (CDN)

This endpoint provides a subset of CDN (Credit Default Notice) data received from ECVAA (Energy Contract Volume Aggregation Agent). It returns the defaults that are in force and defaults that have closed within the last 7 days.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Default notices (CDN)
    api_response = api_instance.get_balancing_settlement_default_notices(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_default_notices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse**](InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate(bid_offer, settlement_date, bm_unit=bm_unit, format=format)

Indicative period BMU cashflows by settlement date (EBOCF)

Returns derived indicative cashflow data generated by the latest calculation run for a given settlement date.                For each settlement period within the range, only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
bid_offer = 'bid_offer_example' # str | Filter if bid or offer data is to be returned.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd.
bm_unit = ['bm_unit_example'] # list[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Indicative period BMU cashflows by settlement date (EBOCF)
    api_response = api_instance.get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate(bid_offer, settlement_date, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid_offer** | **str**| Filter if bid or offer data is to be returned. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **bm_unit** | [**list[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate_se**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate_se(settlement_period, bid_offer, settlement_date, bm_unit=bm_unit, format=format)

Indicative period BMU cashflows by settlement period (EBOCF)

Returns derived indicative cashflow data generated by the latest calculation run for a given settlement period.                Only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_period = 56 # int | Format - int32. The settlement period for the filter.
bid_offer = 'bid_offer_example' # str | Filter if bid or offer data is to be returned.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd.
bm_unit = ['bm_unit_example'] # list[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Indicative period BMU cashflows by settlement period (EBOCF)
    api_response = api_instance.get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate_se(settlement_period, bid_offer, settlement_date, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_indicative_cashflows_all_bidoffer_settlementdate_se: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_period** | **int**| Format - int32. The settlement period for the filter. | 
 **bid_offer** | **str**| Filter if bid or offer data is to be returned. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **bm_unit** | [**list[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate(settlement_date, bid_offer, bm_unit=bm_unit, format=format)

Indicative volumes by settlement date (DISPTAV)

Returns the settlement indicative volumes for the requested settlement date.    For each settlement period within the range, only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd.
bid_offer = 'bid_offer_example' # str | 
bm_unit = ['bm_unit_example'] # list[str] | Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Indicative volumes by settlement date (DISPTAV)
    api_response = api_instance.get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate(settlement_date, bid_offer, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd. | 
 **bid_offer** | **str**|  | 
 **bm_unit** | [**list[str]**](str.md)| Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate_sett**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate_sett(settlement_period, settlement_date, bid_offer, bm_unit=bm_unit, format=format)

Indicative volumes by settlement period (DISPTAV)

Returns the settlement indicative volumes for the requested settlement period.    Only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_period = 56 # int | Format - int32. This should be an integer from 1-50 inclusive.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd.
bid_offer = 'bid_offer_example' # str | 
bm_unit = ['bm_unit_example'] # list[str] | Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Indicative volumes by settlement period (DISPTAV)
    api_response = api_instance.get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate_sett(settlement_period, settlement_date, bid_offer, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_indicative_volumes_all_bidoffer_settlementdate_sett: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_period** | **int**| Format - int32. This should be an integer from 1-50 inclusive. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd. | 
 **bid_offer** | **str**|  | 
 **bm_unit** | [**list[str]**](str.md)| Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_market_depth_settlementdate**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse get_balancing_settlement_market_depth_settlementdate(settlement_date, format=format)

Market depth by settlement date (IMBALNGC, BOD, DISEBSP, DISPTAV)

Returns market depth data for a given day.  Imbalance (MW) is retrieved from IMBALNGC.  Bid/offer volumes (MWh) are calculated by summing bid/offer volumes from BOD.  Total acceptance volumes (MWh) are retrieved from DISEBSP.  Priced acceptance volumes (MWh) are calculated by summing bid/offer accepted volumes with data type Original from DISPTAV.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Market depth by settlement date (IMBALNGC, BOD, DISEBSP, DISPTAV)
    api_response = api_instance.get_balancing_settlement_market_depth_settlementdate(settlement_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_market_depth_settlementdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_market_depth_settlementdate_settlementperiod**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse get_balancing_settlement_market_depth_settlementdate_settlementperiod(settlement_period, settlement_date, format=format)

Market depth by settlement period (IMBALNGC, BOD, DISEBSP, DISPTAV)

Returns market depth data for a given settlement period.  Imbalance (MW) is retrieved from IMBALNGC.  Bid/offer volumes (MWh) are calculated by summing bid/offer volumes from BOD.  Total acceptance volumes (MWh) are retrieved from DISEBSP.  Priced acceptance volumes (MWh) are calculated by summing bid/offer accepted volumes with data type Original from DISPTAV.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_period = 56 # int | Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Market depth by settlement period (IMBALNGC, BOD, DISEBSP, DISPTAV)
    api_response = api_instance.get_balancing_settlement_market_depth_settlementdate_settlementperiod(settlement_period, settlement_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_market_depth_settlementdate_settlementperiod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_period** | **int**| Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_messages_settlementdate**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse get_balancing_settlement_messages_settlementdate(settlement_date, format=format)

Settlement messages by settlement date (SMSG)

Returns settlement messages generated by the SAA for a given settlement day, relating to the data  for a settlement run.                For each settlement period within the range, only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Settlement messages by settlement date (SMSG)
    api_response = api_instance.get_balancing_settlement_messages_settlementdate(settlement_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_messages_settlementdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_messages_settlementdate_settlementperiod**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse get_balancing_settlement_messages_settlementdate_settlementperiod(settlement_period, settlement_date, format=format)

Settlement messages by settlement date and period (SMSG)

Returns settlement messages generated by the SAA for a given settlement period, relating to the data  for a settlement run.                Only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_period = 56 # int | Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Settlement messages by settlement date and period (SMSG)
    api_response = api_instance.get_balancing_settlement_messages_settlementdate_settlementperiod(settlement_period, settlement_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_messages_settlementdate_settlementperiod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_period** | **int**| Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_stack_all_bidoffer_settlementdate_settlementperiod**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementStackResponse get_balancing_settlement_stack_all_bidoffer_settlementdate_settlementperiod(bid_offer, settlement_date, settlement_period, format=format)

Settlement bid-offer stacks by settlement period (ISPSTACK)

Returns detailed system prices generated by the latest calculation run for a given settlement period.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
bid_offer = 'bid_offer_example' # str | Filter if bid or offer data is to be returned.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd.
settlement_period = 56 # int | Format - int32. The settlement period for the filter.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Settlement bid-offer stacks by settlement period (ISPSTACK)
    api_response = api_instance.get_balancing_settlement_stack_all_bidoffer_settlementdate_settlementperiod(bid_offer, settlement_date, settlement_period, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_stack_all_bidoffer_settlementdate_settlementperiod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid_offer** | **str**| Filter if bid or offer data is to be returned. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. This must be in the format yyyy-MM-dd. | 
 **settlement_period** | **int**| Format - int32. The settlement period for the filter. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementStackResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementStackResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_summary_settlementdate_settlementperiod**
> InsightsApiModelsResponsesBalancingSettlementSettlementSummaryResponse get_balancing_settlement_summary_settlementdate_settlementperiod(settlement_date, settlement_period, format=format)

Settlement calculation summary (ISPSTACK, DISEBSP, MID, NETBSAD)

Returns the settlement calculation summary for the requested settlement period.  Data is derived from the following datasets: ISPSTACK, DISEBSP, MID, NETBSAD                In JSON format, decimal values are returned as strings to avoid loss of precision.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd.
settlement_period = 56 # int | Format - int32. This should be an integer from 1-50 inclusive.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Settlement calculation summary (ISPSTACK, DISEBSP, MID, NETBSAD)
    api_response = api_instance.get_balancing_settlement_summary_settlementdate_settlementperiod(settlement_date, settlement_period, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_summary_settlementdate_settlementperiod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). This must be in the format yyyy-MM-dd. | 
 **settlement_period** | **int**| Format - int32. This should be an integer from 1-50 inclusive. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesBalancingSettlementSettlementSummaryResponse**](InsightsApiModelsResponsesBalancingSettlementSettlementSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_system_prices_settlementdate**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse get_balancing_settlement_system_prices_settlementdate(settlement_date, format=format)

Settlement system prices by settlement date (DISEBSP)

Returns settlement system buy and sell prices generated by the SAA for a given settlement day, relating to  the data for a settlement run.                For each settlement period within the range, only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Settlement system prices by settlement date (DISEBSP)
    api_response = api_instance.get_balancing_settlement_system_prices_settlementdate(settlement_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_system_prices_settlementdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_settlement_system_prices_settlementdate_settlementperiod**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse get_balancing_settlement_system_prices_settlementdate_settlementperiod(settlement_period, settlement_date, format=format)

Settlement system prices by settlement date and period (DISEBSP)

Returns settlement system buy and sell prices generated by the SAA for a given settlement period, relating to  the data for a settlement run.                Only messages generated for the latest settlement run are returned.                Settlement date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.IndicativeImbalanceSettlementApi()
settlement_period = 56 # int | Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive.
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Settlement system prices by settlement date and period (DISEBSP)
    api_response = api_instance.get_balancing_settlement_system_prices_settlementdate_settlementperiod(settlement_period, settlement_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicativeImbalanceSettlementApi->get_balancing_settlement_system_prices_settlementdate_settlementperiod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_period** | **int**| Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive. | 
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date to filter. This must be in the format yyyy-MM-dd. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

