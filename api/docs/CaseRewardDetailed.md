# CaseRewardDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**game_id** | **str** |  | 
**user_id** | **str** |  | 
**seen** | **bool** |  | 
**opened** | **bool** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**product** | [**Product**](Product.md) |  | 
**game** | [**Game**](Game.md) |  | 

## Example

```python
from ledge_python_sdk.models.case_reward_detailed import CaseRewardDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of CaseRewardDetailed from a JSON string
case_reward_detailed_instance = CaseRewardDetailed.from_json(json)
# print the JSON string representation of the object
print(CaseRewardDetailed.to_json())

# convert the object into a dict
case_reward_detailed_dict = case_reward_detailed_instance.to_dict()
# create an instance of CaseRewardDetailed from a dict
case_reward_detailed_form_dict = case_reward_detailed.from_dict(case_reward_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


