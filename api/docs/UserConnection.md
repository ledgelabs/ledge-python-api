# UserConnection

Model UserConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**social_id** | **str** |  | 
**social_connection_type** | [**ConnectionType**](ConnectionType.md) |  | 
**nickname** | **str** |  | 
**email** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.user_connection import UserConnection

# TODO update the JSON string below
json = "{}"
# create an instance of UserConnection from a JSON string
user_connection_instance = UserConnection.from_json(json)
# print the JSON string representation of the object
print(UserConnection.to_json())

# convert the object into a dict
user_connection_dict = user_connection_instance.to_dict()
# create an instance of UserConnection from a dict
user_connection_form_dict = user_connection.from_dict(user_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


