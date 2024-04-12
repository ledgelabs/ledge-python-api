# GameTag

Model GameTag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **str** |  | 
**game_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.game_tag import GameTag

# TODO update the JSON string below
json = "{}"
# create an instance of GameTag from a JSON string
game_tag_instance = GameTag.from_json(json)
# print the JSON string representation of the object
print(GameTag.to_json())

# convert the object into a dict
game_tag_dict = game_tag_instance.to_dict()
# create an instance of GameTag from a dict
game_tag_form_dict = game_tag.from_dict(game_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


