# TagDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** |  | 
**icon_url** | **str** |  | 
**label** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**child_tags** | [**List[Tag]**](Tag.md) |  | 

## Example

```python
from ledge_python_sdk.models.tag_detailed import TagDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of TagDetailed from a JSON string
tag_detailed_instance = TagDetailed.from_json(json)
# print the JSON string representation of the object
print(TagDetailed.to_json())

# convert the object into a dict
tag_detailed_dict = tag_detailed_instance.to_dict()
# create an instance of TagDetailed from a dict
tag_detailed_form_dict = tag_detailed.from_dict(tag_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


