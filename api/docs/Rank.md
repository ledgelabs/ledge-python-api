# Rank

Model Rank

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaderboard_id** | **str** |  | 
**rank** | **float** |  | 
**player_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.rank import Rank

# TODO update the JSON string below
json = "{}"
# create an instance of Rank from a JSON string
rank_instance = Rank.from_json(json)
# print the JSON string representation of the object
print(Rank.to_json())

# convert the object into a dict
rank_dict = rank_instance.to_dict()
# create an instance of Rank from a dict
rank_form_dict = rank.from_dict(rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


