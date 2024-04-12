# GoalProduct

Model GoalProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**goal_id** | **str** |  | 
**qty** | **float** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.goal_product import GoalProduct

# TODO update the JSON string below
json = "{}"
# create an instance of GoalProduct from a JSON string
goal_product_instance = GoalProduct.from_json(json)
# print the JSON string representation of the object
print(GoalProduct.to_json())

# convert the object into a dict
goal_product_dict = goal_product_instance.to_dict()
# create an instance of GoalProduct from a dict
goal_product_form_dict = goal_product.from_dict(goal_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


