# NotificationDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**seen** | **bool** |  | 
**object_id** | **str** |  | 
**type** | [**NotificationType**](NotificationType.md) |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**opened** | **bool** |  | 
**var_date** | **datetime** |  | 
**title** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.notification_detailed import NotificationDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDetailed from a JSON string
notification_detailed_instance = NotificationDetailed.from_json(json)
# print the JSON string representation of the object
print(NotificationDetailed.to_json())

# convert the object into a dict
notification_detailed_dict = notification_detailed_instance.to_dict()
# create an instance of NotificationDetailed from a dict
notification_detailed_form_dict = notification_detailed.from_dict(notification_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


