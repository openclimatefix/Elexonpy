# elexonpy.LegacyApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_interop_messagedetailretrieval_messageid_messageid**](LegacyApi.md#get_interop_messagedetailretrieval_messageid_messageid) | **GET** /interop/MessageDetailRetrieval | This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
[**get_interop_messagelistretrieval_eventstart_eventstart_eventend_eventend**](LegacyApi.md#get_interop_messagelistretrieval_eventstart_eventstart_eventend_eventend) | **GET** /interop/MessageListRetrieval | This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.

# **get_interop_messagedetailretrieval_messageid_messageid**
> InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse get_interop_messagedetailretrieval_messageid_messageid(message_id)

This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.

This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.LegacyApi()
message_id = 'message_id_example' # str | 

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
    api_response = api_instance.get_interop_messagedetailretrieval_messageid_messageid(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyApi->get_interop_messagedetailretrieval_messageid_messageid: %s\n" % e)
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

# **get_interop_messagelistretrieval_eventstart_eventstart_eventend_eventend**
> InsightsApiLegacyInteroperabilityLegacyRemitListResponse get_interop_messagelistretrieval_eventstart_eventstart_eventend_eventend(event_start, event_end)

This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.

This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.LegacyApi()
event_start = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).
event_end = '2013-10-20T19:20:30+01:00' # datetime | Format - date-time (as date-time in RFC3339).

try:
    # This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
    api_response = api_instance.get_interop_messagelistretrieval_eventstart_eventstart_eventend_eventend(event_start, event_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyApi->get_interop_messagelistretrieval_eventstart_eventstart_eventend_eventend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_start** | **datetime**| Format - date-time (as date-time in RFC3339). | 
 **event_end** | **datetime**| Format - date-time (as date-time in RFC3339). | 

### Return type

[**InsightsApiLegacyInteroperabilityLegacyRemitListResponse**](InsightsApiLegacyInteroperabilityLegacyRemitListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

