# Screen

Model Screen

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

## Example

```python
from ledge_python_sdk.models.screen import Screen

# TODO update the JSON string below
json = "{}"
# create an instance of Screen from a JSON string
screen_instance = Screen.from_json(json)
# print the JSON string representation of the object
print(Screen.to_json())

# convert the object into a dict
screen_dict = screen_instance.to_dict()
# create an instance of Screen from a dict
screen_form_dict = screen.from_dict(screen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


