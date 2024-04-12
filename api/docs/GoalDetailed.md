# GoalDetailed


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
**quest** | [**Quest**](Quest.md) |  | 
**progress** | [**Progress**](Progress.md) |  | 
**goal_products** | [**List[GoalProductDetailed]**](GoalProductDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.goal_detailed import GoalDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of GoalDetailed from a JSON string
goal_detailed_instance = GoalDetailed.from_json(json)
# print the JSON string representation of the object
print(GoalDetailed.to_json())

# convert the object into a dict
goal_detailed_dict = goal_detailed_instance.to_dict()
# create an instance of GoalDetailed from a dict
goal_detailed_form_dict = goal_detailed.from_dict(goal_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


