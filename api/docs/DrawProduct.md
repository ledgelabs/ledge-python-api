# DrawProduct

Model DrawProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**draw_id** | **str** |  | 
**qty** | **float** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.draw_product import DrawProduct

# TODO update the JSON string below
json = "{}"
# create an instance of DrawProduct from a JSON string
draw_product_instance = DrawProduct.from_json(json)
# print the JSON string representation of the object
print(DrawProduct.to_json())

# convert the object into a dict
draw_product_dict = draw_product_instance.to_dict()
# create an instance of DrawProduct from a dict
draw_product_form_dict = draw_product.from_dict(draw_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


