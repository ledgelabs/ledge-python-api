# ExternalActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.external_activity import ExternalActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalActivity from a JSON string
external_activity_instance = ExternalActivity.from_json(json)
# print the JSON string representation of the object
print(ExternalActivity.to_json())

# convert the object into a dict
external_activity_dict = external_activity_instance.to_dict()
# create an instance of ExternalActivity from a dict
external_activity_form_dict = external_activity.from_dict(external_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


