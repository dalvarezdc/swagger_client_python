# swagger_client.SearchApi

All URIs are relative to *http://127.0.0.1:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](SearchApi.md#search_get) | **GET** /search | Full text search - complete mode
[**search_quick_mode**](SearchApi.md#search_quick_mode) | **GET** /__rm__2/search | Full text search - quick mode
[**suggest2_get**](SearchApi.md#suggest2_get) | **GET** /suggest2 | Suggest2
[**suggest_get**](SearchApi.md#suggest_get) | **GET** /suggest | Suggest
[**terms_get**](SearchApi.md#terms_get) | **GET** /terms | Terms

# **search_get**
> SearchResult search_get(full, text=text, language=language, type=type, is_in_scheme=is_in_scheme, facet=facet, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Full text search - complete mode

# Get all resources of a given class matching a plain text in a given language.  This is a full text search on the preferred labels, the alternative labels, the hidden labels and the description of a resource. The search must be scoped on class type and language. The search result is paged.  Passing parameter full=true, will return a full JSON Object representation of each resource. This implies a higher response time compared to the full text search in quick mode.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
full = true # bool | Set to 'true' to get the full 'HAL' Object representations of the returned resources. (default to true)
text = 'text_example' # str | The text to search for. If omitted all returned resources in the response are ordered by preference label. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
type = ['type_example'] # list[str] | The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. (optional)
is_in_scheme = ['is_in_scheme_example'] # list[str] | The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. (optional)
facet = ['facet_example'] # list[str] | The facet to count for. The reponse will return for each different value of the given facet the number of occurrences in the search result set. Supported facets are 'type' and/or 'isInScheme' (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Full text search - complete mode
    api_response = api_instance.search_get(full, text=text, language=language, type=type, is_in_scheme=is_in_scheme, facet=facet, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **bool**| Set to &#x27;true&#x27; to get the full &#x27;HAL&#x27; Object representations of the returned resources. | [default to true]
 **text** | **str**| The text to search for. If omitted all returned resources in the response are ordered by preference label. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **type** | [**list[str]**](str.md)| The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. | [optional] 
 **is_in_scheme** | [**list[str]**](str.md)| The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. | [optional] 
 **facet** | [**list[str]**](str.md)| The facet to count for. The reponse will return for each different value of the given facet the number of occurrences in the search result set. Supported facets are &#x27;type&#x27; and/or &#x27;isInScheme&#x27; | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_quick_mode**
> SearchResult search_quick_mode(text=text, language=language, type=type, is_in_scheme=is_in_scheme, facet=facet, offset=offset, limit=limit, full=full, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Full text search - quick mode

# Get all resources of a given class matching a plain text in a given language.  This is a full text search on the preferred labels, the alternative labels, the hidden labels and the description of a resource. The search must be scoped on class type and language. The search result is paged.  Passing parameter full=false (or omitting the parameter as false is the default value), will only return a partial JSON Object representation of each resource (~ a fragment). This implies a lower response time compared to the full text search in complete mode.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
text = 'text_example' # str | The text to search for. If omitted all returned resources in the response are ordered by preference label. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
type = ['type_example'] # list[str] | The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. (optional)
is_in_scheme = ['is_in_scheme_example'] # list[str] | The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. (optional)
facet = ['facet_example'] # list[str] | The facet to count for. The reponse will return for each different value of the given facet the number of occurrences in the search result set. Supported facets are 'type' and/or 'isInScheme' (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
full = false # bool | If set to 'true' the full 'HAL' Object representation of each related resource is returned. (optional) (default to false)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Full text search - quick mode
    api_response = api_instance.search_quick_mode(text=text, language=language, type=type, is_in_scheme=is_in_scheme, facet=facet, offset=offset, limit=limit, full=full, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_quick_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to search for. If omitted all returned resources in the response are ordered by preference label. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **type** | [**list[str]**](str.md)| The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. | [optional] 
 **is_in_scheme** | [**list[str]**](str.md)| The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. | [optional] 
 **facet** | [**list[str]**](str.md)| The facet to count for. The reponse will return for each different value of the given facet the number of occurrences in the search result set. Supported facets are &#x27;type&#x27; and/or &#x27;isInScheme&#x27; | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **full** | **bool**| If set to &#x27;true&#x27; the full &#x27;HAL&#x27; Object representation of each related resource is returned. | [optional] [default to false]
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest2_get**
> SuggestionResult suggest2_get(text=text, language=language, type=type, is_in_scheme=is_in_scheme, offset=offset, limit=limit, alt=alt, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Suggest2

# Get all resources of a given class matching a label in a given language.  This is a full text search on the labels of a resource. The search must be scoped on language and optionally on class type. The search result is paged.  This service returns a partial JSON Object representation of each resource (~ a fragment). A typical use of this call is autocomplete.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
text = 'text_example' # str | The text to search for. If omitted all returned resources in the response are ordered by preference label. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
type = ['type_example'] # list[str] | The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. (optional)
is_in_scheme = ['is_in_scheme_example'] # list[str] | The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
alt = false # bool | If set to 'true' both preferred terms and alternative terms are searched (optional) (default to false)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Suggest2
    api_response = api_instance.suggest2_get(text=text, language=language, type=type, is_in_scheme=is_in_scheme, offset=offset, limit=limit, alt=alt, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->suggest2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to search for. If omitted all returned resources in the response are ordered by preference label. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **type** | [**list[str]**](str.md)| The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. | [optional] 
 **is_in_scheme** | [**list[str]**](str.md)| The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **alt** | **bool**| If set to &#x27;true&#x27; both preferred terms and alternative terms are searched | [optional] [default to false]
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**SuggestionResult**](SuggestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest_get**
> SuggestionResult suggest_get(text=text, language=language, type=type, is_in_scheme=is_in_scheme, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Suggest

# Get all resources of a given class matching a preferred label in a given language.  This is a full text search on the preferred label of a resource. The search must be scoped on class type and language. The search result is paged.  This service returns a partial JSON Object representation of each resource (~ a fragment). A typical use of this call is autocomplete.  This method is deprecated. Use instead a new implementation of the suggest service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
text = 'text_example' # str | The text to search for. If omitted all returned resources in the response are ordered by preference label. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
type = ['type_example'] # list[str] | The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. (optional)
is_in_scheme = ['is_in_scheme_example'] # list[str] | The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Suggest
    api_response = api_instance.suggest_get(text=text, language=language, type=type, is_in_scheme=is_in_scheme, offset=offset, limit=limit, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->suggest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to search for. If omitted all returned resources in the response are ordered by preference label. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **type** | [**list[str]**](str.md)| The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. | [optional] 
 **is_in_scheme** | [**list[str]**](str.md)| The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**SuggestionResult**](SuggestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_get**
> TermResult terms_get(text=text, language=language, type=type, is_in_scheme=is_in_scheme, offset=offset, limit=limit, has_label_type=has_label_type, has_label_role=has_label_role, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)

Terms

# Search for individual concept terms matching the given text and language.  This is a full text search. The search result is paged.  This service returns a partial JSON Object representation of each resource (~ a fragment). A typical use of this call is autocomplete.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
text = 'text_example' # str | The text to search for. If omitted all returned resources in the response are ordered by preference label. (optional)
language = 'language_example' # str | The default language of the returned response. Overwrites the Accept-Language header. (optional)
type = ['type_example'] # list[str] | The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. (optional)
is_in_scheme = ['is_in_scheme_example'] # list[str] | The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. (optional)
offset = 0 # int | The offset of the returned resources in the response. Supports paging where the 'offset' specifies the page number (optional) (default to 0)
limit = 20 # int | The maximum number of returned resources in the response. (optional) (default to 20)
has_label_type = ['[\"http://www.w3.org/2008/05/skos-xl#prefLabel\",\"http://www.w3.org/2008/05/skos-xl#altLabel\"]'] # list[str] | The skos-xl property type linking the concept to the label, possible values: ['http://www.w3.org/2008/05/skos-xl#prefLabel', 'http://www.w3.org/2008/05/skos-xl#altLabel', 'http://www.w3.org/2008/05/skos-xl#hiddenLabel'] (optional) (default to ["http://www.w3.org/2008/05/skos-xl#prefLabel","http://www.w3.org/2008/05/skos-xl#altLabel"])
has_label_role = ['has_label_role_example'] # list[str] | Allows filtering on gender specific terms. Value must be the uri of an ESCO label gender role. (optional)
selected_version = 'latest' # str | The selected ESCO dataset version. (optional) (default to latest)
view_obsolete = false # bool | If set to 'true', the obsoleted concepts will be returned (optional) (default to false)
accept_language = 'accept_language_example' # str | The default language of the returned response. Optional and might be overwritten by the language request parameter. (optional)

try:
    # Terms
    api_response = api_instance.terms_get(text=text, language=language, type=type, is_in_scheme=is_in_scheme, offset=offset, limit=limit, has_label_type=has_label_type, has_label_role=has_label_role, selected_version=selected_version, view_obsolete=view_obsolete, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->terms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to search for. If omitted all returned resources in the response are ordered by preference label. | [optional] 
 **language** | **str**| The default language of the returned response. Overwrites the Accept-Language header. | [optional] 
 **type** | [**list[str]**](str.md)| The class of resources to search for. Filter parameter, the search is restricted to resources that belong to at least one of the given classes. | [optional] 
 **is_in_scheme** | [**list[str]**](str.md)| The concept scheme to search for resources that are contained in it. Filter parameter, the search is restricted to resources that are contained in at least one of the given concept schemes. | [optional] 
 **offset** | **int**| The offset of the returned resources in the response. Supports paging where the &#x27;offset&#x27; specifies the page number | [optional] [default to 0]
 **limit** | **int**| The maximum number of returned resources in the response. | [optional] [default to 20]
 **has_label_type** | [**list[str]**](str.md)| The skos-xl property type linking the concept to the label, possible values: [&#x27;http://www.w3.org/2008/05/skos-xl#prefLabel&#x27;, &#x27;http://www.w3.org/2008/05/skos-xl#altLabel&#x27;, &#x27;http://www.w3.org/2008/05/skos-xl#hiddenLabel&#x27;] | [optional] [default to [&quot;http://www.w3.org/2008/05/skos-xl#prefLabel&quot;,&quot;http://www.w3.org/2008/05/skos-xl#altLabel&quot;]]
 **has_label_role** | [**list[str]**](str.md)| Allows filtering on gender specific terms. Value must be the uri of an ESCO label gender role. | [optional] 
 **selected_version** | **str**| The selected ESCO dataset version. | [optional] [default to latest]
 **view_obsolete** | **bool**| If set to &#x27;true&#x27;, the obsoleted concepts will be returned | [optional] [default to false]
 **accept_language** | **str**| The default language of the returned response. Optional and might be overwritten by the language request parameter. | [optional] 

### Return type

[**TermResult**](TermResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

