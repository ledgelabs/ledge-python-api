# NotificationToken

Model NotificationToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**token** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.notification_token import NotificationToken

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationToken from a JSON string
notification_token_instance = NotificationToken.from_json(json)
# print the JSON string representation of the object
print(NotificationToken.to_json())

# convert the object into a dict
notification_token_dict = notification_token_instance.to_dict()
# create an instance of NotificationToken from a dict
notification_token_form_dict = notification_token.from_dict(notification_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


