# elexonpy.ReferenceApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reference_bmunits_all**](ReferenceApi.md#get_reference_bmunits_all) | **GET** /reference/bmunits/all | BM Units
[**get_reference_fueltypes_all**](ReferenceApi.md#get_reference_fueltypes_all) | **GET** /reference/fueltypes/all | Fuel types
[**get_reference_interconnectors_all**](ReferenceApi.md#get_reference_interconnectors_all) | **GET** /reference/interconnectors/all | Interconnectors
[**get_reference_remit_assets_all**](ReferenceApi.md#get_reference_remit_assets_all) | **GET** /reference/remit/assets/all | Assets
[**get_reference_remit_fueltypes_all**](ReferenceApi.md#get_reference_remit_fueltypes_all) | **GET** /reference/remit/fueltypes/all | REMIT fuel types
[**get_reference_remit_participants_all**](ReferenceApi.md#get_reference_remit_participants_all) | **GET** /reference/remit/participants/all | Participants

# **get_reference_bmunits_all**
> list[InsightsApiModelsResponsesReferenceBmUnitData] get_reference_bmunits_all()

BM Units

This endpoint provides a current list of BM units held by Elexon

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.ReferenceApi()

try:
    # BM Units
    api_response = api_instance.get_reference_bmunits_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_reference_bmunits_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InsightsApiModelsResponsesReferenceBmUnitData]**](InsightsApiModelsResponsesReferenceBmUnitData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_fueltypes_all**
> list[str] get_reference_fueltypes_all()

Fuel types

This endpoint provides a current list of fuel types

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.ReferenceApi()

try:
    # Fuel types
    api_response = api_instance.get_reference_fueltypes_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_reference_fueltypes_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_interconnectors_all**
> list[InsightsApiModelsResponsesReferenceInterconnectorData] get_reference_interconnectors_all()

Interconnectors

This endpoint provides a current list of interconnectors

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.ReferenceApi()

try:
    # Interconnectors
    api_response = api_instance.get_reference_interconnectors_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_reference_interconnectors_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InsightsApiModelsResponsesReferenceInterconnectorData]**](InsightsApiModelsResponsesReferenceInterconnectorData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_remit_assets_all**
> list[str] get_reference_remit_assets_all()

Assets

This endpoint provides a current list of asset IDs received from REMIT messages

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.ReferenceApi()

try:
    # Assets
    api_response = api_instance.get_reference_remit_assets_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_reference_remit_assets_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_remit_fueltypes_all**
> list[str] get_reference_remit_fueltypes_all()

REMIT fuel types

This endpoint provides a current list of fuel types received from REMIT messages

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.ReferenceApi()

try:
    # REMIT fuel types
    api_response = api_instance.get_reference_remit_fueltypes_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_reference_remit_fueltypes_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_remit_participants_all**
> list[str] get_reference_remit_participants_all()

Participants

This endpoint provides a current list of participant IDs received from REMIT messages

### Example
```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.ReferenceApi()

try:
    # Participants
    api_response = api_instance.get_reference_remit_participants_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_reference_remit_participants_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

