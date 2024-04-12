# UserQuestDrawDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**goal_product_id** | **str** |  | 
**quest_schedule_id** | **str** |  | 
**user_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**user** | [**User**](User.md) |  | 
**goal_product** | [**GoalProductDetailed**](GoalProductDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.user_quest_draw_detailed import UserQuestDrawDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of UserQuestDrawDetailed from a JSON string
user_quest_draw_detailed_instance = UserQuestDrawDetailed.from_json(json)
# print the JSON string representation of the object
print(UserQuestDrawDetailed.to_json())

# convert the object into a dict
user_quest_draw_detailed_dict = user_quest_draw_detailed_instance.to_dict()
# create an instance of UserQuestDrawDetailed from a dict
user_quest_draw_detailed_form_dict = user_quest_draw_detailed.from_dict(user_quest_draw_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


