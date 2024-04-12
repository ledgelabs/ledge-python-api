# Goal

Model Goal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** |  | 
**quest_id** | **str** |  | 
**activity** | [**ActivityType**](ActivityType.md) |  | 
**banner_url** | **str** |  | 
**target** | **float** |  | 
**instructions** | **str** |  | 
**description** | **str** |  | 
**title** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.goal import Goal

# TODO update the JSON string below
json = "{}"
# create an instance of Goal from a JSON string
goal_instance = Goal.from_json(json)
# print the JSON string representation of the object
print(Goal.to_json())

# convert the object into a dict
goal_dict = goal_instance.to_dict()
# create an instance of Goal from a dict
goal_form_dict = goal.from_dict(goal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


