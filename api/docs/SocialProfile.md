# SocialProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**provider** | [**ConnectionType**](ConnectionType.md) |  | 

## Example

```python
from ledge_python_sdk.models.social_profile import SocialProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SocialProfile from a JSON string
social_profile_instance = SocialProfile.from_json(json)
# print the JSON string representation of the object
print(SocialProfile.to_json())

# convert the object into a dict
social_profile_dict = social_profile_instance.to_dict()
# create an instance of SocialProfile from a dict
social_profile_form_dict = social_profile.from_dict(social_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


