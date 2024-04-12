# PaginatedNotificationDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedCaseRewardDetailedPagination**](PaginatedCaseRewardDetailedPagination.md) |  | 
**data** | [**List[NotificationDetailed]**](NotificationDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.paginated_notification_detailed import PaginatedNotificationDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNotificationDetailed from a JSON string
paginated_notification_detailed_instance = PaginatedNotificationDetailed.from_json(json)
# print the JSON string representation of the object
print(PaginatedNotificationDetailed.to_json())

# convert the object into a dict
paginated_notification_detailed_dict = paginated_notification_detailed_instance.to_dict()
# create an instance of PaginatedNotificationDetailed from a dict
paginated_notification_detailed_form_dict = paginated_notification_detailed.from_dict(paginated_notification_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


