# swagger_client.HistoryApi

All URIs are relative to *http://127.0.0.1:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversion_concept_get**](HistoryApi.md#conversion_concept_get) | **GET** /conversion/concept | Get Converted Concept
[**conversion_occupation_get**](HistoryApi.md#conversion_occupation_get) | **GET** /conversion/occupation | Get Converted Occupation
[**conversion_skill_get**](HistoryApi.md#conversion_skill_get) | **GET** /conversion/skill | Get Converted Skill
[**history_get**](HistoryApi.md#history_get) | **GET** /history | Get history

# **conversion_concept_get**
> Concepts conversion_concept_get(uri, language=language, target_esco_version=target_esco_version, offset=offset, limit=limit, accept_language=accept_language)

Get Converted Concept

# Get a collection of converted resources of class Concept by the universal identifier (~ URI) in the target esco version.  This endpoints finds the state of a given concept on the specified ESCO version. It may return with a collection of concepts if the searched concept was split into more on the expected version.  In order to reconstruct how a concept was split and merged the isReplacedByTransitive relation can be used.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HistoryApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
target_esco_version = 'latest' # str | The target esco version for the converted resource (optional) (default to latest)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get Converted Concept
    api_response = api_instance.conversion_concept_get(uri, language=language, target_esco_version=target_esco_version, offset=offset, limit=limit, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->conversion_concept_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **target_esco_version** | **str**| The target esco version for the converted resource | [optional] [default to latest]
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Concepts**](Concepts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversion_occupation_get**
> Occupations conversion_occupation_get(uri, language=language, target_esco_version=target_esco_version, offset=offset, limit=limit, accept_language=accept_language)

Get Converted Occupation

# Get a collection of converted resources of class Occupation by the universal identifier (~ URI) in the target esco version.  This endpoints finds the state of a given concept on the specified ESCO version. It may return with a collection of concepts if the searched concept was split into more on the expected version.  In order to reconstruct how a concept was split and merged the isReplacedByTransitive relation can be used.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HistoryApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
target_esco_version = 'latest' # str | The target esco version for the converted resource (optional) (default to latest)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get Converted Occupation
    api_response = api_instance.conversion_occupation_get(uri, language=language, target_esco_version=target_esco_version, offset=offset, limit=limit, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->conversion_occupation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **target_esco_version** | **str**| The target esco version for the converted resource | [optional] [default to latest]
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Occupations**](Occupations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversion_skill_get**
> Skills conversion_skill_get(uri, language=language, target_esco_version=target_esco_version, offset=offset, limit=limit, accept_language=accept_language)

Get Converted Skill

# Get a collection of converted resources of class Skill by the universal identifier (~ URI) in the target esco version.  This endpoints finds the state of a given concept on the specified ESCO version. It may return with a collection of concepts if the searched concept was split into more on the expected version.  In order to reconstruct how a concept was split and merged the isReplacedByTransitive relation can be used.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HistoryApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
target_esco_version = 'latest' # str | The target esco version for the converted resource (optional) (default to latest)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get Converted Skill
    api_response = api_instance.conversion_skill_get(uri, language=language, target_esco_version=target_esco_version, offset=offset, limit=limit, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->conversion_skill_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **target_esco_version** | **str**| The target esco version for the converted resource | [optional] [default to latest]
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Skills**](Skills.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history_get**
> str history_get(uri, language=language, full_history=full_history, accept_language=accept_language)

Get history

# Get delta changes of the specified concepts between ESCO version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HistoryApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
full_history = false # bool | If set to 'true' the full history will be returned for all ESCO versions. (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get history
    api_response = api_instance.history_get(uri, language=language, full_history=full_history, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **full_history** | **bool**| If set to &#x27;true&#x27; the full history will be returned for all ESCO versions. | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

