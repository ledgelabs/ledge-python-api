# UserDraw

Model UserDraw

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

## Example

```python
from ledge_python_sdk.models.user_draw import UserDraw

# TODO update the JSON string below
json = "{}"
# create an instance of UserDraw from a JSON string
user_draw_instance = UserDraw.from_json(json)
# print the JSON string representation of the object
print(UserDraw.to_json())

# convert the object into a dict
user_draw_dict = user_draw_instance.to_dict()
# create an instance of UserDraw from a dict
user_draw_form_dict = user_draw.from_dict(user_draw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


