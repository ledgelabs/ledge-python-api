# ConnectedSocial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_inventory** | [**UserInventory**](UserInventory.md) |  | 
**user_connection** | [**UserConnection**](UserConnection.md) |  | 

## Example

```python
from ledge_python_sdk.models.connected_social import ConnectedSocial

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedSocial from a JSON string
connected_social_instance = ConnectedSocial.from_json(json)
# print the JSON string representation of the object
print(ConnectedSocial.to_json())

# convert the object into a dict
connected_social_dict = connected_social_instance.to_dict()
# create an instance of ConnectedSocial from a dict
connected_social_form_dict = connected_social.from_dict(connected_social_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


