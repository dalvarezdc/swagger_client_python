# SuggestionResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of related resources found. | 
**offset** | **int** | The offset of the returned resources. Supports paging where the &#x27;offset&#x27; specifies the page number (zero-based numbering). | [optional] [default to 0]
**limit** | **int** | The maximum number of returned resources. Supports paging where the &#x27;limit&#x27; specifies the maximum page size | [optional] 
**text** | **str** | The text that was searched on. | [optional] 
**language** | **str** | The language of the text that was searched on. | 
**type** | **list[str]** | The class(es) of resources that was searched for. | [optional] 
**is_in_scheme** | **list[str]** | The concept scheme(s) that was searched through. | [optional] 
**facet** | **list[str]** | The counted facet(s) | [optional] 
**links** | [**SuggestionResultLinks**](SuggestionResultLinks.md) |  | [optional] 
**embedded** | [**SuggestionResultEmbedded**](SuggestionResultEmbedded.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

