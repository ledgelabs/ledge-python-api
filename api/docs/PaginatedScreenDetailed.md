# PaginatedScreenDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedCaseRewardDetailedPagination**](PaginatedCaseRewardDetailedPagination.md) |  | 
**data** | [**List[ScreenDetailed]**](ScreenDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.paginated_screen_detailed import PaginatedScreenDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedScreenDetailed from a JSON string
paginated_screen_detailed_instance = PaginatedScreenDetailed.from_json(json)
# print the JSON string representation of the object
print(PaginatedScreenDetailed.to_json())

# convert the object into a dict
paginated_screen_detailed_dict = paginated_screen_detailed_instance.to_dict()
# create an instance of PaginatedScreenDetailed from a dict
paginated_screen_detailed_form_dict = paginated_screen_detailed.from_dict(paginated_screen_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


