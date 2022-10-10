# Resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of resources returned in this collection as _embedded objects. | [default to 0]
**language** | **str** | The default language of the response. | 
**concepts** | [**list[ResourcesConcepts]**](ResourcesConcepts.md) | The main information about resources returned in this collection, detailed information is available in the _embedded map section by the resource URI as a key. | [optional] 
**offset** | **int** | The offset of the returned resources. (zero-based numbering) | [optional] [default to 0]
**total** | **int** | The total number of all available resources regardless the pagination. | [optional] 
**links** | [**ResourcesLinks**](ResourcesLinks.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

