# PaginatedRankDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedCaseRewardDetailedPagination**](PaginatedCaseRewardDetailedPagination.md) |  | 
**data** | [**List[RankDetailed]**](RankDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.paginated_rank_detailed import PaginatedRankDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRankDetailed from a JSON string
paginated_rank_detailed_instance = PaginatedRankDetailed.from_json(json)
# print the JSON string representation of the object
print(PaginatedRankDetailed.to_json())

# convert the object into a dict
paginated_rank_detailed_dict = paginated_rank_detailed_instance.to_dict()
# create an instance of PaginatedRankDetailed from a dict
paginated_rank_detailed_form_dict = paginated_rank_detailed.from_dict(paginated_rank_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


