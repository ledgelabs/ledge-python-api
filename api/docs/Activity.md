# Activity

Model Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurrence** | **datetime** |  | 
**processed** | **bool** |  | 
**count** | **float** |  | 
**object_id** | **str** |  | 
**type** | [**ActivityType**](ActivityType.md) |  | 
**user_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **float** |  | 

## Example

```python
from ledge_python_sdk.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print(Activity.to_json())

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_form_dict = activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


