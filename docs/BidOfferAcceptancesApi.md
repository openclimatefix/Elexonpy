# elexonpy.BidOfferAcceptancesApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balancing_acceptances_acceptancenumber**](BidOfferAcceptancesApi.md#get_balancing_acceptances_acceptancenumber) | **GET** /balancing/acceptances/{acceptanceNumber} | Bid-Offer acceptances by acceptance id
[**get_balancing_acceptances_all_latest**](BidOfferAcceptancesApi.md#get_balancing_acceptances_all_latest) | **GET** /balancing/acceptances/all/latest | Latest market-wide bid-offer acceptances (BOALF)
[**get_balancing_acceptances_all_settlementdate_settlementdate_settlementperiod**](BidOfferAcceptancesApi.md#get_balancing_acceptances_all_settlementdate_settlementdate_settlementperiod) | **GET** /balancing/acceptances/all | Market-wide bid-offer acceptances (BOALF)
[**get_balancing_acceptances_bmunit_bmunit_from_from_to_to**](BidOfferAcceptancesApi.md#get_balancing_acceptances_bmunit_bmunit_from_from_to_to) | **GET** /balancing/acceptances | Bid-offer acceptances per BMU (BOALF)

# **get_balancing_acceptances_acceptancenumber**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse get_balancing_acceptances_acceptancenumber(acceptance_number, format=format)

Bid-Offer acceptances by acceptance id

This endpoint returns bid-offer acceptances for a given acceptance id.  Acceptance ids must be integers.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BidOfferAcceptancesApi()
acceptance_number = 56 # int | Format - int32. The acceptance id to filter results by.
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Bid-Offer acceptances by acceptance id
    api_response = api_instance.get_balancing_acceptances_acceptancenumber(acceptance_number, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BidOfferAcceptancesApi->get_balancing_acceptances_acceptancenumber: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acceptance_number** | **int**| Format - int32. The acceptance id to filter results by. | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_acceptances_all_latest**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse get_balancing_acceptances_all_latest(format=format)

Latest market-wide bid-offer acceptances (BOALF)

This endpoint provides the latest market-wide bid-offer acceptance data (BOALF). The latest 100 acceptances will be returned.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BidOfferAcceptancesApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Latest market-wide bid-offer acceptances (BOALF)
    api_response = api_instance.get_balancing_acceptances_all_latest(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BidOfferAcceptancesApi->get_balancing_acceptances_all_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_acceptances_all_settlementdate_settlementdate_settlementperiod**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse get_balancing_acceptances_all_settlementdate_settlementdate_settlementperiod(settlement_date, settlement_period, bm_unit=bm_unit, format=format)

Market-wide bid-offer acceptances (BOALF)

This endpoint provides the bid-offer acceptance data (BOALF) for multiple requested BMUs or all BMUs.  It returns the data valid for a single settlement period.                The settlement period must be specified as a date and settlement period. The date parameter must be provided in the exact format yyyy-MM-dd.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BidOfferAcceptancesApi()
settlement_date = '2013-10-20' # date | Format - date (as full-date in RFC3339). The settlement date for the filter.
settlement_period = 56 # int | Format - int32. The settlement period for the filter. This should be an integer from 1-50 inclusive.
bm_unit = ['bm_unit_example'] # list[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Market-wide bid-offer acceptances (BOALF)
    api_response = api_instance.get_balancing_acceptances_all_settlementdate_settlementdate_settlementperiod(settlement_date, settlement_period, bm_unit=bm_unit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BidOfferAcceptancesApi->get_balancing_acceptances_all_settlementdate_settlementdate_settlementperiod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| Format - date (as full-date in RFC3339). The settlement date for the filter. | 
 **settlement_period** | **int**| Format - int32. The settlement period for the filter. This should be an integer from 1-50 inclusive. | 
 **bm_unit** | [**list[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancing_acceptances_bmunit_bmunit_from_from_to_to**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse get_balancing_acceptances_bmunit_bmunit_from_from_to_to(bm_unit, _from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Bid-offer acceptances per BMU (BOALF)

This endpoint provides the bid-offer acceptance data (BOALF) for a requested BMU.                By default, the from and to parameters filter the data by start time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of start time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/acceptances?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BidOfferAcceptancesApi()
bm_unit = 'bm_unit_example' # str | The BM Unit to query.
_from = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). The \"from\" start time or settlement date for the filter.
to = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339). The \"to\" start time or settlement date for the filter.
settlement_period_from = 56 # int | Format - int32. The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
settlement_period_to = 56 # int | Format - int32. The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Bid-offer acceptances per BMU (BOALF)
    api_response = api_instance.get_balancing_acceptances_bmunit_bmunit_from_from_to_to(bm_unit, _from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BidOfferAcceptancesApi->get_balancing_acceptances_bmunit_bmunit_from_from_to_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_unit** | **str**| The BM Unit to query. | 
 **_from** | **datetime**| Format - date-time (as date-time in RFC3339). The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| Format - date-time (as date-time in RFC3339). The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| Format - int32. The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| Format - int32. The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

