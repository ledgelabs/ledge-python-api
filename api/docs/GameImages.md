# GameImages

Model GameImages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **str** |  | 
**image_url** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.game_images import GameImages

# TODO update the JSON string below
json = "{}"
# create an instance of GameImages from a JSON string
game_images_instance = GameImages.from_json(json)
# print the JSON string representation of the object
print(GameImages.to_json())

# convert the object into a dict
game_images_dict = game_images_instance.to_dict()
# create an instance of GameImages from a dict
game_images_form_dict = game_images.from_dict(game_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


