# ScreenDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **float** |  | 
**tag_id** | **str** |  | 
**order** | **float** |  | 
**name** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tag** | [**TagDetailed**](TagDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.screen_detailed import ScreenDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenDetailed from a JSON string
screen_detailed_instance = ScreenDetailed.from_json(json)
# print the JSON string representation of the object
print(ScreenDetailed.to_json())

# convert the object into a dict
screen_detailed_dict = screen_detailed_instance.to_dict()
# create an instance of ScreenDetailed from a dict
screen_detailed_form_dict = screen_detailed.from_dict(screen_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


