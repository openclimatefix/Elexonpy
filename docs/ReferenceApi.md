# swagger_client.ReferenceApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reference_bmunits_all_get**](ReferenceApi.md#reference_bmunits_all_get) | **GET** /reference/bmunits/all | BM Units
[**reference_fueltypes_all_get**](ReferenceApi.md#reference_fueltypes_all_get) | **GET** /reference/fueltypes/all | Fuel types
[**reference_interconnectors_all_get**](ReferenceApi.md#reference_interconnectors_all_get) | **GET** /reference/interconnectors/all | Interconnectors
[**reference_remit_assets_all_get**](ReferenceApi.md#reference_remit_assets_all_get) | **GET** /reference/remit/assets/all | Assets
[**reference_remit_fueltypes_all_get**](ReferenceApi.md#reference_remit_fueltypes_all_get) | **GET** /reference/remit/fueltypes/all | REMIT fuel types
[**reference_remit_participants_all_get**](ReferenceApi.md#reference_remit_participants_all_get) | **GET** /reference/remit/participants/all | Participants

# **reference_bmunits_all_get**
> list[InsightsApiModelsResponsesReferenceBmUnitData] reference_bmunits_all_get()

BM Units

This endpoint provides a current list of BM units held by Elexon

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceApi()

try:
    # BM Units
    api_response = api_instance.reference_bmunits_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->reference_bmunits_all_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InsightsApiModelsResponsesReferenceBmUnitData]**](InsightsApiModelsResponsesReferenceBmUnitData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_fueltypes_all_get**
> list[str] reference_fueltypes_all_get()

Fuel types

This endpoint provides a current list of fuel types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceApi()

try:
    # Fuel types
    api_response = api_instance.reference_fueltypes_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->reference_fueltypes_all_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_interconnectors_all_get**
> list[InsightsApiModelsResponsesReferenceInterconnectorData] reference_interconnectors_all_get()

Interconnectors

This endpoint provides a current list of interconnectors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceApi()

try:
    # Interconnectors
    api_response = api_instance.reference_interconnectors_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->reference_interconnectors_all_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InsightsApiModelsResponsesReferenceInterconnectorData]**](InsightsApiModelsResponsesReferenceInterconnectorData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_remit_assets_all_get**
> list[str] reference_remit_assets_all_get()

Assets

This endpoint provides a current list of asset IDs received from REMIT messages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceApi()

try:
    # Assets
    api_response = api_instance.reference_remit_assets_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->reference_remit_assets_all_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_remit_fueltypes_all_get**
> list[str] reference_remit_fueltypes_all_get()

REMIT fuel types

This endpoint provides a current list of fuel types received from REMIT messages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceApi()

try:
    # REMIT fuel types
    api_response = api_instance.reference_remit_fueltypes_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->reference_remit_fueltypes_all_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_remit_participants_all_get**
> list[str] reference_remit_participants_all_get()

Participants

This endpoint provides a current list of participant IDs received from REMIT messages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceApi()

try:
    # Participants
    api_response = api_instance.reference_remit_participants_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->reference_remit_participants_all_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

