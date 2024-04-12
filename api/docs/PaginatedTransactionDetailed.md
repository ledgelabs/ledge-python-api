# PaginatedTransactionDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedCaseRewardDetailedPagination**](PaginatedCaseRewardDetailedPagination.md) |  | 
**data** | [**List[TransactionDetailed]**](TransactionDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.paginated_transaction_detailed import PaginatedTransactionDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTransactionDetailed from a JSON string
paginated_transaction_detailed_instance = PaginatedTransactionDetailed.from_json(json)
# print the JSON string representation of the object
print(PaginatedTransactionDetailed.to_json())

# convert the object into a dict
paginated_transaction_detailed_dict = paginated_transaction_detailed_instance.to_dict()
# create an instance of PaginatedTransactionDetailed from a dict
paginated_transaction_detailed_form_dict = paginated_transaction_detailed.from_dict(paginated_transaction_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


