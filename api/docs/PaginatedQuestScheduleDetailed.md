# PaginatedQuestScheduleDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedCaseRewardDetailedPagination**](PaginatedCaseRewardDetailedPagination.md) |  | 
**data** | [**List[QuestScheduleDetailed]**](QuestScheduleDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.paginated_quest_schedule_detailed import PaginatedQuestScheduleDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQuestScheduleDetailed from a JSON string
paginated_quest_schedule_detailed_instance = PaginatedQuestScheduleDetailed.from_json(json)
# print the JSON string representation of the object
print(PaginatedQuestScheduleDetailed.to_json())

# convert the object into a dict
paginated_quest_schedule_detailed_dict = paginated_quest_schedule_detailed_instance.to_dict()
# create an instance of PaginatedQuestScheduleDetailed from a dict
paginated_quest_schedule_detailed_form_dict = paginated_quest_schedule_detailed.from_dict(paginated_quest_schedule_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


