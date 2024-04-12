# GenreDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** |  | 
**icon_url** | **str** |  | 
**genre** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**sub_genres** | [**List[Genre]**](Genre.md) |  | 

## Example

```python
from ledge_python_sdk.models.genre_detailed import GenreDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of GenreDetailed from a JSON string
genre_detailed_instance = GenreDetailed.from_json(json)
# print the JSON string representation of the object
print(GenreDetailed.to_json())

# convert the object into a dict
genre_detailed_dict = genre_detailed_instance.to_dict()
# create an instance of GenreDetailed from a dict
genre_detailed_form_dict = genre_detailed.from_dict(genre_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


