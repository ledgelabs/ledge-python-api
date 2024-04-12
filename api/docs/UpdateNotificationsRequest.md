# UpdateNotificationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seen** | **bool** |  | 
**notification_ids** | **List[str]** |  | 

## Example

```python
from ledge_python_sdk.models.update_notifications_request import UpdateNotificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationsRequest from a JSON string
update_notifications_request_instance = UpdateNotificationsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationsRequest.to_json())

# convert the object into a dict
update_notifications_request_dict = update_notifications_request_instance.to_dict()
# create an instance of UpdateNotificationsRequest from a dict
update_notifications_request_form_dict = update_notifications_request.from_dict(update_notifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


