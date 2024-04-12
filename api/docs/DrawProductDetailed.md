# DrawProductDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**draw_id** | **str** |  | 
**qty** | **float** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**product** | [**Product**](Product.md) |  | 

## Example

```python
from ledge_python_sdk.models.draw_product_detailed import DrawProductDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of DrawProductDetailed from a JSON string
draw_product_detailed_instance = DrawProductDetailed.from_json(json)
# print the JSON string representation of the object
print(DrawProductDetailed.to_json())

# convert the object into a dict
draw_product_detailed_dict = draw_product_detailed_instance.to_dict()
# create an instance of DrawProductDetailed from a dict
draw_product_detailed_form_dict = draw_product_detailed.from_dict(draw_product_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


