# CreateQuestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.create_quest_request import CreateQuestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestRequest from a JSON string
create_quest_request_instance = CreateQuestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateQuestRequest.to_json())

# convert the object into a dict
create_quest_request_dict = create_quest_request_instance.to_dict()
# create an instance of CreateQuestRequest from a dict
create_quest_request_form_dict = create_quest_request.from_dict(create_quest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


