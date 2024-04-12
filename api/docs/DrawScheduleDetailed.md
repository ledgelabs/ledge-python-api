# DrawScheduleDetailed


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
**draw** | [**DrawDetailed**](DrawDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.draw_schedule_detailed import DrawScheduleDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of DrawScheduleDetailed from a JSON string
draw_schedule_detailed_instance = DrawScheduleDetailed.from_json(json)
# print the JSON string representation of the object
print(DrawScheduleDetailed.to_json())

# convert the object into a dict
draw_schedule_detailed_dict = draw_schedule_detailed_instance.to_dict()
# create an instance of DrawScheduleDetailed from a dict
draw_schedule_detailed_form_dict = draw_schedule_detailed.from_dict(draw_schedule_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


