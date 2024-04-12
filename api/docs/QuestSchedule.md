# QuestSchedule

Model QuestSchedule

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

## Example

```python
from ledge_python_sdk.models.quest_schedule import QuestSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of QuestSchedule from a JSON string
quest_schedule_instance = QuestSchedule.from_json(json)
# print the JSON string representation of the object
print(QuestSchedule.to_json())

# convert the object into a dict
quest_schedule_dict = quest_schedule_instance.to_dict()
# create an instance of QuestSchedule from a dict
quest_schedule_form_dict = quest_schedule.from_dict(quest_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


