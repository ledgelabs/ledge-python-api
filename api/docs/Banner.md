# Banner

Model Banner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**subtitle** | **str** |  | 
**title** | **str** |  | 
**end_time** | **datetime** |  | 
**start_time** | **datetime** |  | 
**game_id** | **str** |  | 
**alt** | **str** |  | 
**url** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.banner import Banner

# TODO update the JSON string below
json = "{}"
# create an instance of Banner from a JSON string
banner_instance = Banner.from_json(json)
# print the JSON string representation of the object
print(Banner.to_json())

# convert the object into a dict
banner_dict = banner_instance.to_dict()
# create an instance of Banner from a dict
banner_form_dict = banner.from_dict(banner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


