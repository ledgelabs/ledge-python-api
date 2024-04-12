# UserDrawDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**draw_product_id** | **str** |  | 
**draw_schedule_id** | **str** |  | 
**user_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**draw_product** | [**DrawProductDetailed**](DrawProductDetailed.md) |  | 
**user** | [**User**](User.md) |  | 

## Example

```python
from ledge_python_sdk.models.user_draw_detailed import UserDrawDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of UserDrawDetailed from a JSON string
user_draw_detailed_instance = UserDrawDetailed.from_json(json)
# print the JSON string representation of the object
print(UserDrawDetailed.to_json())

# convert the object into a dict
user_draw_detailed_dict = user_draw_detailed_instance.to_dict()
# create an instance of UserDrawDetailed from a dict
user_draw_detailed_form_dict = user_draw_detailed.from_dict(user_draw_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


