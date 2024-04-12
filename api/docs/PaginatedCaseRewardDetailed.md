# PaginatedCaseRewardDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedCaseRewardDetailedPagination**](PaginatedCaseRewardDetailedPagination.md) |  | 
**data** | [**List[CaseRewardDetailed]**](CaseRewardDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.paginated_case_reward_detailed import PaginatedCaseRewardDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCaseRewardDetailed from a JSON string
paginated_case_reward_detailed_instance = PaginatedCaseRewardDetailed.from_json(json)
# print the JSON string representation of the object
print(PaginatedCaseRewardDetailed.to_json())

# convert the object into a dict
paginated_case_reward_detailed_dict = paginated_case_reward_detailed_instance.to_dict()
# create an instance of PaginatedCaseRewardDetailed from a dict
paginated_case_reward_detailed_form_dict = paginated_case_reward_detailed.from_dict(paginated_case_reward_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


