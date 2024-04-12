# GameTagDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **str** |  | 
**game_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tag** | [**TagDetailed**](TagDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.game_tag_detailed import GameTagDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of GameTagDetailed from a JSON string
game_tag_detailed_instance = GameTagDetailed.from_json(json)
# print the JSON string representation of the object
print(GameTagDetailed.to_json())

# convert the object into a dict
game_tag_detailed_dict = game_tag_detailed_instance.to_dict()
# create an instance of GameTagDetailed from a dict
game_tag_detailed_form_dict = game_tag_detailed.from_dict(game_tag_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


