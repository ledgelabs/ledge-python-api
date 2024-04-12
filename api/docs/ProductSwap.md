# ProductSwap

Model ProductSwap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swappable_product_id** | **str** |  | 
**product_id** | **str** |  | 
**chance** | **float** |  | 
**qty** | **float** |  | 
**title** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.product_swap import ProductSwap

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSwap from a JSON string
product_swap_instance = ProductSwap.from_json(json)
# print the JSON string representation of the object
print(ProductSwap.to_json())

# convert the object into a dict
product_swap_dict = product_swap_instance.to_dict()
# create an instance of ProductSwap from a dict
product_swap_form_dict = product_swap.from_dict(product_swap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


