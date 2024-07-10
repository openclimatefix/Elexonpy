# swagger_client.REMITApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remit_get**](REMITApi.md#remit_get) | **GET** /remit | Bulk fetch message details by IDs
[**remit_list_by_event_get**](REMITApi.md#remit_list_by_event_get) | **GET** /remit/list/by-event | List messages by event time
[**remit_list_by_event_stream_get**](REMITApi.md#remit_list_by_event_stream_get) | **GET** /remit/list/by-event/stream | List messages by event time (stream)
[**remit_list_by_publish_get**](REMITApi.md#remit_list_by_publish_get) | **GET** /remit/list/by-publish | List messages by publish time
[**remit_list_by_publish_stream_get**](REMITApi.md#remit_list_by_publish_stream_get) | **GET** /remit/list/by-publish/stream | List messages by publish time (stream)
[**remit_message_id_get**](REMITApi.md#remit_message_id_get) | **GET** /remit/{messageId} | Fetch message details by ID
[**remit_revisions_get**](REMITApi.md#remit_revisions_get) | **GET** /remit/revisions | List all message revisions
[**remit_search_get**](REMITApi.md#remit_search_get) | **GET** /remit/search | Fetch message details by mRID

# **remit_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId remit_get(message_id, format=format)

Bulk fetch message details by IDs

This endpoint provides one or more REMIT messages based on the given message IDs.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.REMITApi()
message_id = [56]  # list[int] | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Bulk fetch message details by IDs
    api_response = api_instance.remit_get(message_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling REMITApi->remit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | [**list[int]**](int.md)|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remit_list_by_event_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl remit_list_by_event_get(_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only, format=format)

List messages by event time

This endpoint provides a list of REMIT message identifiers based on the event start time, end time and other optional parameters.                - Filtering by LatestRevisionOnly (default = true):     if true, include only the latest revision of each message.                - Filtering by ProfileOnly (default = false):      if true, include only messages with an outage profile.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.REMITApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
participant_id = 'participant_id_example'  # str |  (optional)
asset_id = 'asset_id_example'  # str |  (optional)
message_type = 'message_type_example'  # str |  (optional)
unavailability_type = 'unavailability_type_example'  # str |  (optional)
event_type = ['event_type_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
latest_revision_only = true  # bool |  (optional)
profile_only = true  # bool |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # List messages by event time
    api_response = api_instance.remit_list_by_event_get(_from, to, participant_id=participant_id, asset_id=asset_id,
                                                        message_type=message_type,
                                                        unavailability_type=unavailability_type, event_type=event_type,
                                                        fuel_type=fuel_type, latest_revision_only=latest_revision_only,
                                                        profile_only=profile_only, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling REMITApi->remit_list_by_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **participant_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **message_type** | **str**|  | [optional] 
 **unavailability_type** | **str**|  | [optional] 
 **event_type** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **latest_revision_only** | **bool**|  | [optional] 
 **profile_only** | **bool**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remit_list_by_event_stream_get**
> list[InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl] remit_list_by_event_stream_get(_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only)

List messages by event time (stream)

This endpoint provides a list of REMIT message identifiers based on the event start, end time and other optional parameters.                - Filtering by LatestRevisionOnly (default = true):     if true, include only the latest revision of each message.                - Filtering by ProfileOnly (default = false):      if true, include only messages with an outage profile.                This endpoint has an optimised JSON payload and is aimed at frequent requests for this data.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.REMITApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
participant_id = 'participant_id_example'  # str |  (optional)
asset_id = 'asset_id_example'  # str |  (optional)
message_type = 'message_type_example'  # str |  (optional)
unavailability_type = 'unavailability_type_example'  # str |  (optional)
event_type = ['event_type_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
latest_revision_only = true  # bool |  (optional)
profile_only = true  # bool |  (optional)

try:
    # List messages by event time (stream)
    api_response = api_instance.remit_list_by_event_stream_get(_from, to, participant_id=participant_id,
                                                               asset_id=asset_id, message_type=message_type,
                                                               unavailability_type=unavailability_type,
                                                               event_type=event_type, fuel_type=fuel_type,
                                                               latest_revision_only=latest_revision_only,
                                                               profile_only=profile_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling REMITApi->remit_list_by_event_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **participant_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **message_type** | **str**|  | [optional] 
 **unavailability_type** | **str**|  | [optional] 
 **event_type** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **latest_revision_only** | **bool**|  | [optional] 
 **profile_only** | **bool**|  | [optional] 

### Return type

[**list[InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl]**](InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remit_list_by_publish_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl remit_list_by_publish_get(_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only, format=format)

List messages by publish time

This endpoint provides a list of REMIT message identifiers based on the publish time and other optional parameters.                - Filtering by LatestRevisionOnly (default = true):     if true, include only the latest revision of each message.                - Filtering by ProfileOnly (default = false):      if true, include only messages with an outage profile.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.REMITApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
participant_id = 'participant_id_example'  # str |  (optional)
asset_id = 'asset_id_example'  # str |  (optional)
message_type = 'message_type_example'  # str |  (optional)
unavailability_type = 'unavailability_type_example'  # str |  (optional)
event_type = ['event_type_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
latest_revision_only = true  # bool |  (optional)
profile_only = true  # bool |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # List messages by publish time
    api_response = api_instance.remit_list_by_publish_get(_from, to, participant_id=participant_id, asset_id=asset_id,
                                                          message_type=message_type,
                                                          unavailability_type=unavailability_type,
                                                          event_type=event_type, fuel_type=fuel_type,
                                                          latest_revision_only=latest_revision_only,
                                                          profile_only=profile_only, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling REMITApi->remit_list_by_publish_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **participant_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **message_type** | **str**|  | [optional] 
 **unavailability_type** | **str**|  | [optional] 
 **event_type** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **latest_revision_only** | **bool**|  | [optional] 
 **profile_only** | **bool**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remit_list_by_publish_stream_get**
> list[InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl] remit_list_by_publish_stream_get(_from, to, participant_id=participant_id, asset_id=asset_id, message_type=message_type, unavailability_type=unavailability_type, event_type=event_type, fuel_type=fuel_type, latest_revision_only=latest_revision_only, profile_only=profile_only)

List messages by publish time (stream)

This endpoint provides a list of REMIT message identifiers based on the publish time and other optional parameters.                - Filtering by LatestRevisionOnly (default = true):     if true, include only the latest revision of each message.                - Filtering by ProfileOnly (default = false):      if true, include only messages with an outage profile.                This endpoint has an optimised JSON payload and is aimed at frequent requests for this data.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.REMITApi()
_from = '2013-10-20T19:20:30+01:00'  # datetime | 
to = '2013-10-20T19:20:30+01:00'  # datetime | 
participant_id = 'participant_id_example'  # str |  (optional)
asset_id = 'asset_id_example'  # str |  (optional)
message_type = 'message_type_example'  # str |  (optional)
unavailability_type = 'unavailability_type_example'  # str |  (optional)
event_type = ['event_type_example']  # list[str] |  (optional)
fuel_type = ['fuel_type_example']  # list[str] |  (optional)
latest_revision_only = true  # bool |  (optional)
profile_only = true  # bool |  (optional)

try:
    # List messages by publish time (stream)
    api_response = api_instance.remit_list_by_publish_stream_get(_from, to, participant_id=participant_id,
                                                                 asset_id=asset_id, message_type=message_type,
                                                                 unavailability_type=unavailability_type,
                                                                 event_type=event_type, fuel_type=fuel_type,
                                                                 latest_revision_only=latest_revision_only,
                                                                 profile_only=profile_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling REMITApi->remit_list_by_publish_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **participant_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **message_type** | **str**|  | [optional] 
 **unavailability_type** | **str**|  | [optional] 
 **event_type** | [**list[str]**](str.md)|  | [optional] 
 **fuel_type** | [**list[str]**](str.md)|  | [optional] 
 **latest_revision_only** | **bool**|  | [optional] 
 **profile_only** | **bool**|  | [optional] 

### Return type

[**list[InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl]**](InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remit_message_id_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId remit_message_id_get(message_id, format=format)

Fetch message details by ID

This endpoint provides a REMIT message based on a given message ID.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.REMITApi()
message_id = 56  # int | 
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Fetch message details by ID
    api_response = api_instance.remit_message_id_get(message_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling REMITApi->remit_message_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**|  | 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remit_revisions_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl remit_revisions_get(mrid=mrid, message_id=message_id, format=format)

List all message revisions

This endpoint provides all revisions for a given REMIT message.  The message can be specified in two ways:  - the mRID  - the message ID of a specific revision, which will return the entire list of revisions for that message

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.REMITApi()
mrid = 'mrid_example'  # str |  (optional)
message_id = 56  # int |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # List all message revisions
    api_response = api_instance.remit_revisions_get(mrid=mrid, message_id=message_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling REMITApi->remit_revisions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mrid** | **str**|  | [optional] 
 **message_id** | **int**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remit_search_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId remit_search_get(mrid, revision_number=revision_number, format=format)

Fetch message details by mRID

This endpoint provides one or more REMIT messages based on the given mRID and revision number. If none is given  it returns the REMIT message revision with the latest revision number.

### Example

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.REMITApi()
mrid = 'mrid_example'  # str | 
revision_number = 56  # int |  (optional)
format = 'format_example'  # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Fetch message details by mRID
    api_response = api_instance.remit_search_get(mrid, revision_number=revision_number, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling REMITApi->remit_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mrid** | **str**|  | 
 **revision_number** | **int**|  | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

