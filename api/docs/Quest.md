# Quest

Model Quest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**QuestType**](QuestType.md) |  | 
**description** | **str** |  | 
**title** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.quest import Quest

# TODO update the JSON string below
json = "{}"
# create an instance of Quest from a JSON string
quest_instance = Quest.from_json(json)
# print the JSON string representation of the object
print(Quest.to_json())

# convert the object into a dict
quest_dict = quest_instance.to_dict()
# create an instance of Quest from a dict
quest_form_dict = quest.from_dict(quest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


