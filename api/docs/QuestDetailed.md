# QuestDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**QuestType**](QuestType.md) |  | 
**description** | **str** |  | 
**title** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**goals** | [**List[GoalDetailed]**](GoalDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.quest_detailed import QuestDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of QuestDetailed from a JSON string
quest_detailed_instance = QuestDetailed.from_json(json)
# print the JSON string representation of the object
print(QuestDetailed.to_json())

# convert the object into a dict
quest_detailed_dict = quest_detailed_instance.to_dict()
# create an instance of QuestDetailed from a dict
quest_detailed_form_dict = quest_detailed.from_dict(quest_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


