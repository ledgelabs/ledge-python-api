# DrawDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired_ticket_id** | **str** |  | 
**ticket_id** | **str** |  | 
**object_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**expired_ticket** | [**Product**](Product.md) |  | 
**draw_products** | [**List[DrawProductDetailed]**](DrawProductDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.draw_detailed import DrawDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of DrawDetailed from a JSON string
draw_detailed_instance = DrawDetailed.from_json(json)
# print the JSON string representation of the object
print(DrawDetailed.to_json())

# convert the object into a dict
draw_detailed_dict = draw_detailed_instance.to_dict()
# create an instance of DrawDetailed from a dict
draw_detailed_form_dict = draw_detailed.from_dict(draw_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


