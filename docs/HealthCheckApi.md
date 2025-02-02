# swagger_client.HealthCheckApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](HealthCheckApi.md#get_health) | **GET** /health | Health check

# **get_health**
> get_health()

Health check

This endpoint provides a success response code (200) with status code 2 if the service is alive

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthCheckApi()

try:
    # Health check
    api_instance.get_health()
except ApiException as e:
    print("Exception when calling HealthCheckApi->get_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

