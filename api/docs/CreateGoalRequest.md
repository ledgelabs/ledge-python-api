# CreateGoalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **str** |  | 
**quest_id** | **str** |  | 
**banner_url** | **str** |  | [optional] 
**target** | **float** |  | 
**instruction** | **str** |  | [optional] 
**description** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.create_goal_request import CreateGoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGoalRequest from a JSON string
create_goal_request_instance = CreateGoalRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGoalRequest.to_json())

# convert the object into a dict
create_goal_request_dict = create_goal_request_instance.to_dict()
# create an instance of CreateGoalRequest from a dict
create_goal_request_form_dict = create_goal_request.from_dict(create_goal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


