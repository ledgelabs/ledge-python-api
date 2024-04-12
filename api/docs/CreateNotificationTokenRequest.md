# CreateNotificationTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.create_notification_token_request import CreateNotificationTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationTokenRequest from a JSON string
create_notification_token_request_instance = CreateNotificationTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationTokenRequest.to_json())

# convert the object into a dict
create_notification_token_request_dict = create_notification_token_request_instance.to_dict()
# create an instance of CreateNotificationTokenRequest from a dict
create_notification_token_request_form_dict = create_notification_token_request.from_dict(create_notification_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


