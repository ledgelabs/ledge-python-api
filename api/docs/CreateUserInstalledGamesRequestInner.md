# CreateUserInstalledGamesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_name** | **str** |  | 
**first_installed_time** | **float** |  | 

## Example

```python
from ledge_python_sdk.models.create_user_installed_games_request_inner import CreateUserInstalledGamesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserInstalledGamesRequestInner from a JSON string
create_user_installed_games_request_inner_instance = CreateUserInstalledGamesRequestInner.from_json(json)
# print the JSON string representation of the object
print(CreateUserInstalledGamesRequestInner.to_json())

# convert the object into a dict
create_user_installed_games_request_inner_dict = create_user_installed_games_request_inner_instance.to_dict()
# create an instance of CreateUserInstalledGamesRequestInner from a dict
create_user_installed_games_request_inner_form_dict = create_user_installed_games_request_inner.from_dict(create_user_installed_games_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


