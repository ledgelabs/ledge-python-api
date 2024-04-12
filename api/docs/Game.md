# Game

Model Game

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_store_id** | **str** |  | 
**app_store_id** | **str** |  | 
**logo_url** | **str** |  | 
**banner_url** | **str** |  | 
**banner_title** | **str** |  | 
**icon_url** | **str** |  | 
**description** | **str** |  | 
**title** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.game import Game

# TODO update the JSON string below
json = "{}"
# create an instance of Game from a JSON string
game_instance = Game.from_json(json)
# print the JSON string representation of the object
print(Game.to_json())

# convert the object into a dict
game_dict = game_instance.to_dict()
# create an instance of Game from a dict
game_form_dict = game.from_dict(game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


