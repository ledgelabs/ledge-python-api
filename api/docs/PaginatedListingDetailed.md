# PaginatedListingDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedCaseRewardDetailedPagination**](PaginatedCaseRewardDetailedPagination.md) |  | 
**data** | [**List[ListingDetailed]**](ListingDetailed.md) |  | 

## Example

```python
from ledge_python_sdk.models.paginated_listing_detailed import PaginatedListingDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedListingDetailed from a JSON string
paginated_listing_detailed_instance = PaginatedListingDetailed.from_json(json)
# print the JSON string representation of the object
print(PaginatedListingDetailed.to_json())

# convert the object into a dict
paginated_listing_detailed_dict = paginated_listing_detailed_instance.to_dict()
# create an instance of PaginatedListingDetailed from a dict
paginated_listing_detailed_form_dict = paginated_listing_detailed.from_dict(paginated_listing_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


