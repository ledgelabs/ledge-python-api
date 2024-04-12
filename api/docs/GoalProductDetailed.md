# GoalProductDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**goal_id** | **str** |  | 
**qty** | **float** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**redeemed** | **bool** |  | 
**product** | [**Product**](Product.md) |  | 

## Example

```python
from ledge_python_sdk.models.goal_product_detailed import GoalProductDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of GoalProductDetailed from a JSON string
goal_product_detailed_instance = GoalProductDetailed.from_json(json)
# print the JSON string representation of the object
print(GoalProductDetailed.to_json())

# convert the object into a dict
goal_product_detailed_dict = goal_product_detailed_instance.to_dict()
# create an instance of GoalProductDetailed from a dict
goal_product_detailed_form_dict = goal_product_detailed.from_dict(goal_product_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


