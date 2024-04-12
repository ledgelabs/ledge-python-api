# MergeAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_id** | **str** |  | [optional] 

## Example

```python
from ledge_python_sdk.models.merge_account_request import MergeAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeAccountRequest from a JSON string
merge_account_request_instance = MergeAccountRequest.from_json(json)
# print the JSON string representation of the object
print(MergeAccountRequest.to_json())

# convert the object into a dict
merge_account_request_dict = merge_account_request_instance.to_dict()
# create an instance of MergeAccountRequest from a dict
merge_account_request_form_dict = merge_account_request.from_dict(merge_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


