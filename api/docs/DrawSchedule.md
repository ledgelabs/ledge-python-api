# DrawSchedule

Model DrawSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed** | **bool** |  | 
**draw_id** | **str** |  | 
**recurring** | **bool** |  | 
**end_time** | **datetime** |  | 
**start_time** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.draw_schedule import DrawSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DrawSchedule from a JSON string
draw_schedule_instance = DrawSchedule.from_json(json)
# print the JSON string representation of the object
print(DrawSchedule.to_json())

# convert the object into a dict
draw_schedule_dict = draw_schedule_instance.to_dict()
# create an instance of DrawSchedule from a dict
draw_schedule_form_dict = draw_schedule.from_dict(draw_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


