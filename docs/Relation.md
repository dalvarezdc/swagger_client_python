# Relation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of related resources found. | 
**offset** | **int** | The offset of the returned resources. Supports paging where the &#x27;offset&#x27; specifies the page number (zero-based numbering). | [optional] [default to 0]
**limit** | **int** | The maximum number of returned resources. Supports paging where the &#x27;limit&#x27; specifies the maximum page size | [optional] 
**language** | **str** | The default language of the response. | 
**uri** | **str** | The uri of the resource to get related resources from. | 
**relation** | **str** | The relation to query related resources for. | 
**links** | [**RelationLinks**](RelationLinks.md) |  | [optional] 
**embedded** | [**RelationEmbedded**](RelationEmbedded.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

