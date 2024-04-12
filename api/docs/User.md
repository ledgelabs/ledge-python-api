# User

Model User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_login** | **datetime** |  | 
**verified** | **bool** |  | 
**merged_with** | **str** |  | 
**game_id** | **str** |  | 
**external_id** | **str** |  | 
**referred_by_id** | **str** |  | 
**enable_notifications** | **bool** |  | 
**has_accepted_legal** | **bool** |  | 
**has_onboarded** | **bool** |  | 
**gender** | [**Gender**](Gender.md) |  | 
**birth_year** | **float** |  | 
**avatar** | **str** |  | 
**remaining_referrals** | **float** |  | 
**code** | **str** |  | 
**usertag** | **float** |  | 
**username** | **str** |  | 
**name** | **str** |  | 
**phone_number** | **str** |  | 
**email** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from ledge_python_sdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


