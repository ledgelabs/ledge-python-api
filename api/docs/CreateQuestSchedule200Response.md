# CreateQuestSchedule200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quest_schedule** | [**QuestSchedule**](QuestSchedule.md) |  | [optional] 
**message** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.create_quest_schedule200_response import CreateQuestSchedule200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestSchedule200Response from a JSON string
create_quest_schedule200_response_instance = CreateQuestSchedule200Response.from_json(json)
# print the JSON string representation of the object
print(CreateQuestSchedule200Response.to_json())

# convert the object into a dict
create_quest_schedule200_response_dict = create_quest_schedule200_response_instance.to_dict()
# create an instance of CreateQuestSchedule200Response from a dict
create_quest_schedule200_response_form_dict = create_quest_schedule200_response.from_dict(create_quest_schedule200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


