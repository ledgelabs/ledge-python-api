# UserInventoryDetailed


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
**user** | [**User**](User.md) |  | 
**product** | [**Product**](Product.md) |  | 

## Example

```python
from ledge_python_sdk.models.user_inventory_detailed import UserInventoryDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of UserInventoryDetailed from a JSON string
user_inventory_detailed_instance = UserInventoryDetailed.from_json(json)
# print the JSON string representation of the object
print(UserInventoryDetailed.to_json())

# convert the object into a dict
user_inventory_detailed_dict = user_inventory_detailed_instance.to_dict()
# create an instance of UserInventoryDetailed from a dict
user_inventory_detailed_form_dict = user_inventory_detailed.from_dict(user_inventory_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


