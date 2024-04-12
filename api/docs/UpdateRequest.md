# UpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_notifications** | **bool** |  | [optional] 
**has_accepted_legal** | **bool** |  | [optional] 
**has_onboarded** | **bool** |  | [optional] 
**gender** | [**Gender**](Gender.md) |  | [optional] 
**birth_year** | **float** |  | [optional] 
**merged_with** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from ledge_python_sdk.models.update_request import UpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRequest from a JSON string
update_request_instance = UpdateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRequest.to_json())

# convert the object into a dict
update_request_dict = update_request_instance.to_dict()
# create an instance of UpdateRequest from a dict
update_request_form_dict = update_request.from_dict(update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


