# swagger_client.HealthCheckApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get**](HealthCheckApi.md#health_get) | **GET** /health | Health check

# **health_get**
> health_get()

Health check

This endpoint provides a success status code (200) if the service is alive

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.HealthCheckApi()

try:
    # Health check
    api_instance.health_get()
except ApiException as e:
    print("Exception when calling HealthCheckApi->health_get: %s\n" % e)
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

