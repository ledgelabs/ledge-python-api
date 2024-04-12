# CreateQuestScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurring** | **bool** |  | 
**quest_id** | **str** |  | 
**end_time** | **datetime** |  | 
**start_time** | **datetime** |  | 

## Example

```python
from ledge_python_sdk.models.create_quest_schedule_request import CreateQuestScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestScheduleRequest from a JSON string
create_quest_schedule_request_instance = CreateQuestScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateQuestScheduleRequest.to_json())

# convert the object into a dict
create_quest_schedule_request_dict = create_quest_schedule_request_instance.to_dict()
# create an instance of CreateQuestScheduleRequest from a dict
create_quest_schedule_request_form_dict = create_quest_schedule_request.from_dict(create_quest_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


