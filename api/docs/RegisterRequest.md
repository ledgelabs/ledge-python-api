# RegisterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**game_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**sub** | **str** |  | [optional] 
**username** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.register_request import RegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterRequest from a JSON string
register_request_instance = RegisterRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterRequest.to_json())

# convert the object into a dict
register_request_dict = register_request_instance.to_dict()
# create an instance of RegisterRequest from a dict
register_request_form_dict = register_request.from_dict(register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


