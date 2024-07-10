# swagger_client.BidOfferApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balancing_bid_offer_all_get**](BidOfferApi.md#balancing_bid_offer_all_get) | **GET** /balancing/bid-offer/all | Market-wide bid-offer data (BOD)
[**balancing_bid_offer_get**](BidOfferApi.md#balancing_bid_offer_get) | **GET** /balancing/bid-offer | Bid-offer data per BMU (BOD)

# **balancing_bid_offer_all_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse balancing_bid_offer_all_get(settlement_date, settlement_period, bm_unit=bm_unit, format=format)

Market-wide bid-offer data (BOD)

This endpoint provides market-wide bid-offer data, for all BMUs or a requested set of multiple BMUs.  It returns the data valid for a given settlement period, excluding any results where LevelFrom and LevelTo are both zero.                The settlement period to query must be specified as a date and settlement period. The date should be provided in the format yyyy-MM-dd.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BidOfferApi()
settlement_date = '2013-10-20'  # date | The settlement date to filter.
settlement_period = 56  # int | The settlement period to filter. This should be an integer from 1-50 inclusive.
bm_unit = [
    'bm_unit_example']  # list[str] | The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Market-wide bid-offer data (BOD)
    api_response = api_instance.balancing_bid_offer_all_get(settlement_date, settlement_period, bm_unit=bm_unit,
                                                            format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BidOfferApi->balancing_bid_offer_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_date** | **date**| The settlement date to filter. | 
 **settlement_period** | **int**| The settlement period to filter. This should be an integer from 1-50 inclusive. | 
 **bm_unit** | [**list[str]**](str.md)| The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balancing_bid_offer_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse balancing_bid_offer_get(bm_unit, _from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Bid-offer data per BMU (BOD)

This endpoint provides the bid-offer data for a requested BMU. It returns the data valid over a given time  range, excluding any results where LevelFrom and LevelTo are both zero.                By default, the from and to parameters filter the data inclusively and this endpoint will return any data that  overlaps even at a single instant. If the settlementPeriodFrom or settlementPeriodTo parameters are provided, it  will instead filter to return any data that overlaps with the specified range of settlement periods. It is  possible to search using a combination of time and/or settlement date & settlement period. Note: When  filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For example,  2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering by timeFrom and timeTo:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from timeFrom to settlement date and period:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to TimeTo:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.BidOfferApi()
bm_unit = 'bm_unit_example'  # str | The BM Unit to query.
_from = '2013-10-20T19:20:30+01:00'  # datetime | The \"from\" start time or settlement date for the filter.
to = '2013-10-20T19:20:30+01:00'  # datetime | The \"to\" start time or settlement date for the filter.
settlement_period_from = 56  # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
settlement_period_to = 56  # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Bid-offer data per BMU (BOD)
    api_response = api_instance.balancing_bid_offer_get(bm_unit, _from, to,
                                                        settlement_period_from=settlement_period_from,
                                                        settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BidOfferApi->balancing_bid_offer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_unit** | **str**| The BM Unit to query. | 
 **_from** | **datetime**| The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

