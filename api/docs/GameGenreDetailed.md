# GameGenreDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genre_id** | **str** |  | 
**game_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**genre** | [**Genre**](Genre.md) |  | 

## Example

```python
from ledge_python_sdk.models.game_genre_detailed import GameGenreDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of GameGenreDetailed from a JSON string
game_genre_detailed_instance = GameGenreDetailed.from_json(json)
# print the JSON string representation of the object
print(GameGenreDetailed.to_json())

# convert the object into a dict
game_genre_detailed_dict = game_genre_detailed_instance.to_dict()
# create an instance of GameGenreDetailed from a dict
game_genre_detailed_form_dict = game_genre_detailed.from_dict(game_genre_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


