# GameDetailed


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
**game_tags** | [**List[GameTagDetailed]**](GameTagDetailed.md) |  | 
**game_genres** | [**List[GameGenreDetailed]**](GameGenreDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.game_detailed import GameDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of GameDetailed from a JSON string
game_detailed_instance = GameDetailed.from_json(json)
# print the JSON string representation of the object
print(GameDetailed.to_json())

# convert the object into a dict
game_detailed_dict = game_detailed_instance.to_dict()
# create an instance of GameDetailed from a dict
game_detailed_form_dict = game_detailed.from_dict(game_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


