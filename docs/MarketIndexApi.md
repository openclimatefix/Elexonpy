# swagger_client.MarketIndexApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balancing_pricing_market_index_get**](MarketIndexApi.md#balancing_pricing_market_index_get) | **GET** /balancing/pricing/market-index | Market Index Data (MID) price time series

# **balancing_pricing_market_index_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse balancing_pricing_market_index_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, data_providers=data_providers, format=format)

Market Index Data (MID) price time series

This endpoint provides Market Index Data received from NGESO.                Market Index Data is a key component in the calculation of System Buy Price and System Sell Price for each  Settlement Period. This data is received from each of the appointed Market Index Data Providers (MIDPs) and  reflects the price of wholesale electricity in Great Britain in the short term markets. The Market Index Data  which is received from each MIDP for each Settlement Period consists of a Market Index Volume and  Market Index Price, representing the volume and price of trading for the relevant period in the market operated  by the MIDP. The Market Price (the volume weighed average Market Index Price) is used to derive  the Reverse Price (SBP or SSP).\"                The two data providers available to query are N2EX (\"N2EXMIDP\") and APX (\"APXMIDP\").    By default, the from and to parameters filter the data by time inclusively. If the settlementPeriodFrom or  settlementPeriodTo parameters are provided, the corresponding from or to parameter instead filters on settlement  date, allowing for searching by a combination of time and/or settlement date & settlement period.  Note: When filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For  example, 2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering from start time to start time:                    /balancing/pricing/market-index?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from start time to settlement date and period:                    /balancing/pricing/market-index?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to start time:                    /balancing/pricing/market-index?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/pricing/market-index?from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketIndexApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | The \"from\" start time or settlement date for the filter.
to = '2013-10-20T19:20:30+01:00' # datetime | The \"to\" start time or settlement date for the filter.
settlement_period_from = 56 # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
settlement_period_to = 56 # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
data_providers = ['data_providers_example'] # list[str] | The data providers to query. If no data provider is selected both will be displayed. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Market Index Data (MID) price time series
    api_response = api_instance.balancing_pricing_market_index_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, data_providers=data_providers, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketIndexApi->balancing_pricing_market_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| The \&quot;from\&quot; start time or settlement date for the filter. | 
 **to** | **datetime**| The \&quot;to\&quot; start time or settlement date for the filter. | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **data_providers** | [**list[str]**](str.md)| The data providers to query. If no data provider is selected both will be displayed. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

