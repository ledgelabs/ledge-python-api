# PaginatedCaseRewardDetailedPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **float** |  | 
**current_page** | **float** |  | 
**page_size** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from ledge_python_sdk.models.paginated_case_reward_detailed_pagination import PaginatedCaseRewardDetailedPagination

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCaseRewardDetailedPagination from a JSON string
paginated_case_reward_detailed_pagination_instance = PaginatedCaseRewardDetailedPagination.from_json(json)
# print the JSON string representation of the object
print(PaginatedCaseRewardDetailedPagination.to_json())

# convert the object into a dict
paginated_case_reward_detailed_pagination_dict = paginated_case_reward_detailed_pagination_instance.to_dict()
# create an instance of PaginatedCaseRewardDetailedPagination from a dict
paginated_case_reward_detailed_pagination_form_dict = paginated_case_reward_detailed_pagination.from_dict(paginated_case_reward_detailed_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


