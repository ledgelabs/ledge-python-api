# GameGenre

Model GameGenre

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genre_id** | **str** |  | 
**game_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.game_genre import GameGenre

# TODO update the JSON string below
json = "{}"
# create an instance of GameGenre from a JSON string
game_genre_instance = GameGenre.from_json(json)
# print the JSON string representation of the object
print(GameGenre.to_json())

# convert the object into a dict
game_genre_dict = game_genre_instance.to_dict()
# create an instance of GameGenre from a dict
game_genre_form_dict = game_genre.from_dict(game_genre_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


