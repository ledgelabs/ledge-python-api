# ListingDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_per_user_period** | [**PeriodType**](PeriodType.md) |  | 
**limit_per_user** | **float** |  | 
**claimed_qty** | **float** |  | 
**cost** | **float** |  | 
**cost_type** | [**ProductType**](ProductType.md) |  | 
**qty_available** | **float** |  | 
**product_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**product** | [**Product**](Product.md) |  | 

## Example

```python
from ledge_python_sdk.models.listing_detailed import ListingDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of ListingDetailed from a JSON string
listing_detailed_instance = ListingDetailed.from_json(json)
# print the JSON string representation of the object
print(ListingDetailed.to_json())

# convert the object into a dict
listing_detailed_dict = listing_detailed_instance.to_dict()
# create an instance of ListingDetailed from a dict
listing_detailed_form_dict = listing_detailed.from_dict(listing_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


