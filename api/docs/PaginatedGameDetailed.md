# PaginatedGameDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedCaseRewardDetailedPagination**](PaginatedCaseRewardDetailedPagination.md) |  | 
**data** | [**List[GameDetailed]**](GameDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.paginated_game_detailed import PaginatedGameDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGameDetailed from a JSON string
paginated_game_detailed_instance = PaginatedGameDetailed.from_json(json)
# print the JSON string representation of the object
print(PaginatedGameDetailed.to_json())

# convert the object into a dict
paginated_game_detailed_dict = paginated_game_detailed_instance.to_dict()
# create an instance of PaginatedGameDetailed from a dict
paginated_game_detailed_form_dict = paginated_game_detailed.from_dict(paginated_game_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


