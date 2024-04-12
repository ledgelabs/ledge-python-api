# QuestScheduleDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurring** | **bool** |  | 
**processed** | **bool** |  | 
**quest_id** | **str** |  | 
**end_time** | **datetime** |  | 
**start_time** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**quest** | [**QuestDetailed**](QuestDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.quest_schedule_detailed import QuestScheduleDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of QuestScheduleDetailed from a JSON string
quest_schedule_detailed_instance = QuestScheduleDetailed.from_json(json)
# print the JSON string representation of the object
print(QuestScheduleDetailed.to_json())

# convert the object into a dict
quest_schedule_detailed_dict = quest_schedule_detailed_instance.to_dict()
# create an instance of QuestScheduleDetailed from a dict
quest_schedule_detailed_form_dict = quest_schedule_detailed.from_dict(quest_schedule_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


