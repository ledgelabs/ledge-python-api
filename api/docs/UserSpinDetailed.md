# UserSpinDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** |  | 
**seen** | **bool** |  | 
**qty** | **float** |  | 
**product_id** | **str** |  | 
**user_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**transactions** | [**List[Transaction]**](Transaction.md) |  | 
**game** | [**Game**](Game.md) |  | 
**product** | [**Product**](Product.md) |  | 

## Example

```python
from ledge_python_sdk.models.user_spin_detailed import UserSpinDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of UserSpinDetailed from a JSON string
user_spin_detailed_instance = UserSpinDetailed.from_json(json)
# print the JSON string representation of the object
print(UserSpinDetailed.to_json())

# convert the object into a dict
user_spin_detailed_dict = user_spin_detailed_instance.to_dict()
# create an instance of UserSpinDetailed from a dict
user_spin_detailed_form_dict = user_spin_detailed.from_dict(user_spin_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


