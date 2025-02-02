# swagger_client.CreditDefaultNoticeApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cdn**](CreditDefaultNoticeApi.md#get_cdn) | **GET** /CDN | [DEPRECATED] Credit default notices (CDN)

# **get_cdn**
> get_cdn(format=format)

[DEPRECATED] Credit default notices (CDN)

This endpoint has been moved to balancing/settlement/default-notices.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditDefaultNoticeApi()
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # [DEPRECATED] Credit default notices (CDN)
    api_instance.get_cdn(format=format)
except ApiException as e:
    print("Exception when calling CreditDefaultNoticeApi->get_cdn: %s\n" % e)
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

