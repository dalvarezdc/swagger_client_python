# swagger_client.SingleConceptApi

All URIs are relative to *http://127.0.0.1:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_concept_get**](SingleConceptApi.md#resource_concept_get) | **GET** /resource/concept | Get concept
[**resource_occupation_get**](SingleConceptApi.md#resource_occupation_get) | **GET** /resource/occupation | Get occupation
[**resource_skill_get**](SingleConceptApi.md#resource_skill_get) | **GET** /resource/skill | Get skill
[**resource_taxonomy_get**](SingleConceptApi.md#resource_taxonomy_get) | **GET** /resource/taxonomy | Get concept scheme

# **resource_concept_get**
> Concept resource_concept_get(uri, language=language, selected_version=selected_version, accept_language=accept_language)

Get concept

# Get a resource of class Concept by its universal identifier (~ a URI).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SingleConceptApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get concept
    api_response = api_instance.resource_concept_get(uri, language=language, selected_version=selected_version, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SingleConceptApi->resource_concept_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Concept**](Concept.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_occupation_get**
> Occupation resource_occupation_get(uri, language=language, selected_version=selected_version, accept_language=accept_language)

Get occupation

# Get a resource of class Occupation by its universal identifier (~ a URI).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SingleConceptApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get occupation
    api_response = api_instance.resource_occupation_get(uri, language=language, selected_version=selected_version, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SingleConceptApi->resource_occupation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Occupation**](Occupation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_skill_get**
> Skill resource_skill_get(uri, language=language, selected_version=selected_version, accept_language=accept_language)

Get skill

# Get a resource of class Skill by its universal identifier (~ a URI).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SingleConceptApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get skill
    api_response = api_instance.resource_skill_get(uri, language=language, selected_version=selected_version, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SingleConceptApi->resource_skill_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Skill**](Skill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_taxonomy_get**
> Taxonomy resource_taxonomy_get(uri, language=language, selected_version=selected_version, accept_language=accept_language)

Get concept scheme

# Get a resource of class Taxonomy (~ a concept scheme) by its universal identifier (~ a URI).  This service can be used as entry point for hierarchical display of ESCO resources. The returned Taxonomy resource includes links to the top level concepts within the concept hierarchy of the concept scheme.  ESCO organizes different 'kind' of concept resources in different concept schemes. Concepts come in compiled vocabularies, such as thesauri or classification schemes. Concepts might also be grouped or organised into collections.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SingleConceptApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get concept scheme
    api_response = api_instance.resource_taxonomy_get(uri, language=language, selected_version=selected_version, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SingleConceptApi->resource_taxonomy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Taxonomy**](Taxonomy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

