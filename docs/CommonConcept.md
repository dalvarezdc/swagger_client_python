# CommonConcept

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_language** | **list[str]** | The reference language is the default language in which the information about the occupation is provided. The value of this field is an array containing ISO 639-1 two-letter language codes. | 
**description** | [**dict(str, TextNode)**](TextNode.md) | The description of the concept. The value of this field is a map containing Text Nodes indexed by language. | [optional] 
**definition** | [**dict(str, TextNode)**](TextNode.md) | An abstract description of the concept. The value of this field is a map containing Text Nodes indexed by language. | [optional] 
**scope_note** | [**dict(str, TextNode)**](TextNode.md) | A scope note about the concept. The value of this field is a map containing Text Nodes indexed by language. | [optional] 
**status** | **str** | The publication status of the concept. The value of this field is a string indicating the publication status. | 
**links** | [**CommonConceptLinks**](CommonConceptLinks.md) |  | [optional] 
**embedded** | [**CommonConceptEmbedded**](CommonConceptEmbedded.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

