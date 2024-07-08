# swagger_client.LegacyApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**interop_message_detail_retrieval_get**](LegacyApi.md#interop_message_detail_retrieval_get) | **GET** /interop/MessageDetailRetrieval | This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
[**interop_message_list_retrieval_get**](LegacyApi.md#interop_message_list_retrieval_get) | **GET** /interop/MessageListRetrieval | This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.

# **interop_message_detail_retrieval_get**
> InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse interop_message_detail_retrieval_get(message_id)

This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LegacyApi()
message_id = 'message_id_example' # str | 

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
    api_response = api_instance.interop_message_detail_retrieval_get(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyApi->interop_message_detail_retrieval_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 

### Return type

[**InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse**](InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interop_message_list_retrieval_get**
> InsightsApiLegacyInteroperabilityLegacyRemitListResponse interop_message_list_retrieval_get(event_start, event_end)

This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LegacyApi()
event_start = '2013-10-20T19:20:30+01:00' # datetime | 
event_end = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
    api_response = api_instance.interop_message_list_retrieval_get(event_start, event_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyApi->interop_message_list_retrieval_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_start** | **datetime**|  | 
 **event_end** | **datetime**|  | 

### Return type

[**InsightsApiLegacyInteroperabilityLegacyRemitListResponse**](InsightsApiLegacyInteroperabilityLegacyRemitListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

