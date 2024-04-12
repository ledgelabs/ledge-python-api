# TransactionDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**StatusType**](StatusType.md) |  | 
**object_id** | **str** |  | 
**sell_product_quantity** | **float** |  | 
**sell_product_id** | **str** |  | 
**buy_product_quantity** | **float** |  | 
**buy_product_id** | **str** |  | 
**transaction_type** | [**TransactionType**](TransactionType.md) |  | 
**user_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**sell_product** | [**Product**](Product.md) |  | 
**buy_product** | [**Product**](Product.md) |  | 

## Example

```python
from ledge_python_sdk.models.transaction_detailed import TransactionDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetailed from a JSON string
transaction_detailed_instance = TransactionDetailed.from_json(json)
# print the JSON string representation of the object
print(TransactionDetailed.to_json())

# convert the object into a dict
transaction_detailed_dict = transaction_detailed_instance.to_dict()
# create an instance of TransactionDetailed from a dict
transaction_detailed_form_dict = transaction_detailed.from_dict(transaction_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


