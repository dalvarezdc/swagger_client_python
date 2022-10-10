# swagger_client.BulkOperationApi

All URIs are relative to *http://127.0.0.1:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concept_by_concept_scheme**](BulkOperationApi.md#get_concept_by_concept_scheme) | **GET** /__rm__3/resource/concept | Get concepts - by Concept Scheme
[**get_concept_by_uri**](BulkOperationApi.md#get_concept_by_uri) | **GET** /__rm__2/resource/concept | Get concepts - by URIs
[**get_occupation_by_concept_scheme**](BulkOperationApi.md#get_occupation_by_concept_scheme) | **GET** /__rm__3/resource/occupation | Get occupations - by Concept Scheme
[**get_occupation_by_uri**](BulkOperationApi.md#get_occupation_by_uri) | **GET** /__rm__2/resource/occupation | Get occupations - by URIs
[**get_skill_by_concept_scheme**](BulkOperationApi.md#get_skill_by_concept_scheme) | **GET** /__rm__3/resource/skill | Get skills - by Concept Scheme
[**get_skill_by_uri**](BulkOperationApi.md#get_skill_by_uri) | **GET** /__rm__2/resource/skill | Get skills - by URIs
[**get_taxonomy_by_uri**](BulkOperationApi.md#get_taxonomy_by_uri) | **GET** /__rm__2/resource/taxonomy | Get concept schemes - by URIs
[**resource_related_get**](BulkOperationApi.md#resource_related_get) | **GET** /resource/related | Get related resources

# **get_concept_by_concept_scheme**
> Concepts get_concept_by_concept_scheme(is_in_scheme, language=language, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Get concepts - by Concept Scheme

# Get a collection of resources of class Concept by the universal identifier (~ URI) of a Concept Scheme.  This service is a bulk operation on the Get concept service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkOperationApi()
is_in_scheme = 'is_in_scheme_example' # str | The unique identifier of the requested concept scheme.
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get concepts - by Concept Scheme
    api_response = api_instance.get_concept_by_concept_scheme(is_in_scheme, language=language, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkOperationApi->get_concept_by_concept_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_in_scheme** | **str**| The unique identifier of the requested concept scheme. | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Concepts**](Concepts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept_by_uri**
> Concepts get_concept_by_uri(curie=curie, uris=uris, language=language, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Get concepts - by URIs

# Get a collection of resources of class Concept by their universal identifiers (~ URIs).  This service is a bulk operation on the Get concept service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkOperationApi()
curie = 'curie_example' # str | The prefix of the provided URIs as parameters. CURIE (or Compact URI) defines a generic, abbreviated syntax for expressing Uniform Resource Identifiers (URIs). (optional)
uris = ['uris_example'] # list[str] | The array of unique identifiers of the requested resources or the array of the end of unique identifiers if CURIE is defined. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get concepts - by URIs
    api_response = api_instance.get_concept_by_uri(curie=curie, uris=uris, language=language, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkOperationApi->get_concept_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curie** | **str**| The prefix of the provided URIs as parameters. CURIE (or Compact URI) defines a generic, abbreviated syntax for expressing Uniform Resource Identifiers (URIs). | [optional] 
 **uris** | [**list[str]**](str.md)| The array of unique identifiers of the requested resources or the array of the end of unique identifiers if CURIE is defined. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Concepts**](Concepts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_occupation_by_concept_scheme**
> Occupations get_occupation_by_concept_scheme(is_in_scheme, language=language, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Get occupations - by Concept Scheme

# Get a collection of resources of class Occupation by the universal identifier (~ URI) of a Concept Scheme.  This service is a bulk operation on the Get occupation service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkOperationApi()
is_in_scheme = 'is_in_scheme_example' # str | The unique identifier of the requested concept scheme.
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get occupations - by Concept Scheme
    api_response = api_instance.get_occupation_by_concept_scheme(is_in_scheme, language=language, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkOperationApi->get_occupation_by_concept_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_in_scheme** | **str**| The unique identifier of the requested concept scheme. | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Occupations**](Occupations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_occupation_by_uri**
> Occupations get_occupation_by_uri(curie=curie, uris=uris, language=language, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Get occupations - by URIs

# Get a collection of resources of class Occupation by their universal identifiers (~ URIs).  This service is a bulk operation on the Get occupation service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkOperationApi()
curie = 'curie_example' # str | The prefix of the provided URIs as parameters. CURIE (or Compact URI) defines a generic, abbreviated syntax for expressing Uniform Resource Identifiers (URIs). (optional)
uris = ['uris_example'] # list[str] | The array of unique identifiers of the requested resources or the array of the end of unique identifiers if CURIE is defined. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get occupations - by URIs
    api_response = api_instance.get_occupation_by_uri(curie=curie, uris=uris, language=language, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkOperationApi->get_occupation_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curie** | **str**| The prefix of the provided URIs as parameters. CURIE (or Compact URI) defines a generic, abbreviated syntax for expressing Uniform Resource Identifiers (URIs). | [optional] 
 **uris** | [**list[str]**](str.md)| The array of unique identifiers of the requested resources or the array of the end of unique identifiers if CURIE is defined. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Occupations**](Occupations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_skill_by_concept_scheme**
> Skills get_skill_by_concept_scheme(is_in_scheme, language=language, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Get skills - by Concept Scheme

# Get a collection of resources of class Skill by the universal identifier (~ URI) of a Concept Scheme.  This service is a bulk operation on the Get skill service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkOperationApi()
is_in_scheme = 'is_in_scheme_example' # str | The unique identifier of the requested concept scheme.
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get skills - by Concept Scheme
    api_response = api_instance.get_skill_by_concept_scheme(is_in_scheme, language=language, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkOperationApi->get_skill_by_concept_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_in_scheme** | **str**| The unique identifier of the requested concept scheme. | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Skills**](Skills.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_skill_by_uri**
> Skills get_skill_by_uri(curie=curie, uris=uris, language=language, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Get skills - by URIs

# Get a collection of resources of class Skill by their universal identifiers (~ URIs).  This service is a bulk operation on the Get skill service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkOperationApi()
curie = 'curie_example' # str | The prefix of the provided URIs as parameters. CURIE (or Compact URI) defines a generic, abbreviated syntax for expressing Uniform Resource Identifiers (URIs). (optional)
uris = ['uris_example'] # list[str] | The array of unique identifiers of the requested resources or the array of the end of unique identifiers if CURIE is defined. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get skills - by URIs
    api_response = api_instance.get_skill_by_uri(curie=curie, uris=uris, language=language, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkOperationApi->get_skill_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curie** | **str**| The prefix of the provided URIs as parameters. CURIE (or Compact URI) defines a generic, abbreviated syntax for expressing Uniform Resource Identifiers (URIs). | [optional] 
 **uris** | [**list[str]**](str.md)| The array of unique identifiers of the requested resources or the array of the end of unique identifiers if CURIE is defined. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Skills**](Skills.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxonomy_by_uri**
> Taxonomies get_taxonomy_by_uri(curie=curie, uris=uris, language=language, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Get concept schemes - by URIs

# Get a collection of resources of class Taxonomy (~ a concept scheme) by their universal identifiers (~ URIs).  This service can be used as entry point for hierarchical display of ESCO resources. The returned Taxonomy resources include links to the top level concepts within the concept hierarchy of the concept scheme.  This service is a bulk operation on the Get concept scheme service.  **When curie parameter is defined then all the values in the uris list are prefixed by the CURIE value automatically and the twovalues together should provide real URIs of resources.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkOperationApi()
curie = 'curie_example' # str | The prefix of the provided URIs as parameters. CURIE (or Compact URI) defines a generic, abbreviated syntax for expressing Uniform Resource Identifiers (URIs). (optional)
uris = ['uris_example'] # list[str] | The array of unique identifiers of the requested resources or the array of the end of unique identifiers if CURIE is defined. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get concept schemes - by URIs
    api_response = api_instance.get_taxonomy_by_uri(curie=curie, uris=uris, language=language, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkOperationApi->get_taxonomy_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curie** | **str**| The prefix of the provided URIs as parameters. CURIE (or Compact URI) defines a generic, abbreviated syntax for expressing Uniform Resource Identifiers (URIs). | [optional] 
 **uris** | [**list[str]**](str.md)| The array of unique identifiers of the requested resources or the array of the end of unique identifiers if CURIE is defined. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Taxonomies**](Taxonomies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_related_get**
> Relation resource_related_get(uri, relation, language=language, offset=offset, limit=limit, full=full, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Get related resources

# Get the related resources of a given resource by a given relation.  By default a partial JSON Object representation of each related resource (~ a fragment) is returned. Passing the parameter 'full=true', will return a full JSON Object representation of each resource but this implies a higher response time.  **Remark**: For concept resources (classes Occupation, Skill, Concept) an additional relation hasBroaderTransitive is supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkOperationApi()
uri = 'uri_example' # str | The unique identifier of the requested resource
relation = 'relation_example' # str | The relation to get the related resources for. Must be a known relation of the class the resource belongs to.
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
full = false # bool | If set to 'true' the full 'HAL' Object representation of each related resource is returned. (optional) (default to false)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Get related resources
    api_response = api_instance.resource_related_get(uri, relation, language=language, offset=offset, limit=limit, full=full, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkOperationApi->resource_related_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The unique identifier of the requested resource | 
 **relation** | **str**| The relation to get the related resources for. Must be a known relation of the class the resource belongs to. | 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **full** | **bool**| If set to &#x27;true&#x27; the full &#x27;HAL&#x27; Object representation of each related resource is returned. | [optional] [default to false]
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**Relation**](Relation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

