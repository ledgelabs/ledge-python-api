# RankDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaderboard_id** | **str** |  | 
**rank** | **float** |  | 
**player_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**stats** | [**List[PlayerStats]**](PlayerStats.md) |  | 
**player** | [**User**](User.md) |  | 

## Example

```python
from ledge_python_sdk.models.rank_detailed import RankDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of RankDetailed from a JSON string
rank_detailed_instance = RankDetailed.from_json(json)
# print the JSON string representation of the object
print(RankDetailed.to_json())

# convert the object into a dict
rank_detailed_dict = rank_detailed_instance.to_dict()
# create an instance of RankDetailed from a dict
rank_detailed_form_dict = rank_detailed.from_dict(rank_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


