# Draw

Model Draw

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired_ticket_id** | **str** |  | 
**ticket_id** | **str** |  | 
**object_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.draw import Draw

# TODO update the JSON string below
json = "{}"
# create an instance of Draw from a JSON string
draw_instance = Draw.from_json(json)
# print the JSON string representation of the object
print(Draw.to_json())

# convert the object into a dict
draw_dict = draw_instance.to_dict()
# create an instance of Draw from a dict
draw_form_dict = draw.from_dict(draw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


