# CaseReward

Model CaseReward

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

## Example

```python
from ledge_python_sdk.models.case_reward import CaseReward

# TODO update the JSON string below
json = "{}"
# create an instance of CaseReward from a JSON string
case_reward_instance = CaseReward.from_json(json)
# print the JSON string representation of the object
print(CaseReward.to_json())

# convert the object into a dict
case_reward_dict = case_reward_instance.to_dict()
# create an instance of CaseReward from a dict
case_reward_form_dict = case_reward.from_dict(case_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


