# ProcessedDrawSchedule


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
**user_draws** | [**List[UserDrawDetailed]**](UserDrawDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.processed_draw_schedule import ProcessedDrawSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedDrawSchedule from a JSON string
processed_draw_schedule_instance = ProcessedDrawSchedule.from_json(json)
# print the JSON string representation of the object
print(ProcessedDrawSchedule.to_json())

# convert the object into a dict
processed_draw_schedule_dict = processed_draw_schedule_instance.to_dict()
# create an instance of ProcessedDrawSchedule from a dict
processed_draw_schedule_form_dict = processed_draw_schedule.from_dict(processed_draw_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


