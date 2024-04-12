# UserInventory

Model UserInventory

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

## Example

```python
from ledge_python_sdk.models.user_inventory import UserInventory

# TODO update the JSON string below
json = "{}"
# create an instance of UserInventory from a JSON string
user_inventory_instance = UserInventory.from_json(json)
# print the JSON string representation of the object
print(UserInventory.to_json())

# convert the object into a dict
user_inventory_dict = user_inventory_instance.to_dict()
# create an instance of UserInventory from a dict
user_inventory_form_dict = user_inventory.from_dict(user_inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


