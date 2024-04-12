# ExternalUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.external_user import ExternalUser

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalUser from a JSON string
external_user_instance = ExternalUser.from_json(json)
# print the JSON string representation of the object
print(ExternalUser.to_json())

# convert the object into a dict
external_user_dict = external_user_instance.to_dict()
# create an instance of ExternalUser from a dict
external_user_form_dict = external_user.from_dict(external_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


