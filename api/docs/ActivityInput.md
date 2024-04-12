# ActivityInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** |  | [optional] 
**object_id** | **str** |  | 
**activity** | [**ActivityType**](ActivityType.md) |  | 

## Example

```python
from ledge_python_sdk.models.activity_input import ActivityInput

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityInput from a JSON string
activity_input_instance = ActivityInput.from_json(json)
# print the JSON string representation of the object
print(ActivityInput.to_json())

# convert the object into a dict
activity_input_dict = activity_input_instance.to_dict()
# create an instance of ActivityInput from a dict
activity_input_form_dict = activity_input.from_dict(activity_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


