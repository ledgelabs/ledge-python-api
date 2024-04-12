# ledge_python_sdk.ExternalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_goal**](ExternalApi.md#create_goal) | **POST** /external/{key}/goal | 
[**create_quest**](ExternalApi.md#create_quest) | **POST** /external/quests | 
[**create_quest_schedule**](ExternalApi.md#create_quest_schedule) | **POST** /external/{key}/questSchedule | 
[**get_external_user**](ExternalApi.md#get_external_user) | **GET** /external/{key}/external-user | 
[**get_my_goals**](ExternalApi.md#get_my_goals) | **GET** /external/my-goals | 
[**get_my_quests**](ExternalApi.md#get_my_quests) | **GET** /external/my-quests | 
[**register_user**](ExternalApi.md#register_user) | **POST** /external/{key}/user | 
[**track_activity**](ExternalApi.md#track_activity) | **POST** /external/{key}/activity | 


# **create_goal**
> TrackActivity200Response create_goal(key, create_goal_request)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.create_goal_request import CreateGoalRequest
from ledge_python_sdk.models.track_activity200_response import TrackActivity200Response
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.ExternalApi(api_client)
    key = 'key_example' # str | 
    create_goal_request = ledge_python_sdk.CreateGoalRequest() # CreateGoalRequest | 

    try:
        api_response = api_instance.create_goal(key, create_goal_request)
        print("The response of ExternalApi->create_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->create_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **create_goal_request** | [**CreateGoalRequest**](CreateGoalRequest.md)|  | 

### Return type

[**TrackActivity200Response**](TrackActivity200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quest**
> TrackActivity200Response create_quest(api_key, create_quest_request)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.create_quest_request import CreateQuestRequest
from ledge_python_sdk.models.track_activity200_response import TrackActivity200Response
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.ExternalApi(api_client)
    api_key = 'api_key_example' # str | 
    create_quest_request = ledge_python_sdk.CreateQuestRequest() # CreateQuestRequest | 

    try:
        api_response = api_instance.create_quest(api_key, create_quest_request)
        print("The response of ExternalApi->create_quest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->create_quest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **create_quest_request** | [**CreateQuestRequest**](CreateQuestRequest.md)|  | 

### Return type

[**TrackActivity200Response**](TrackActivity200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quest_schedule**
> CreateQuestSchedule200Response create_quest_schedule(key, create_quest_schedule_request)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.create_quest_schedule200_response import CreateQuestSchedule200Response
from ledge_python_sdk.models.create_quest_schedule_request import CreateQuestScheduleRequest
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.ExternalApi(api_client)
    key = 'key_example' # str | 
    create_quest_schedule_request = ledge_python_sdk.CreateQuestScheduleRequest() # CreateQuestScheduleRequest | 

    try:
        api_response = api_instance.create_quest_schedule(key, create_quest_schedule_request)
        print("The response of ExternalApi->create_quest_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->create_quest_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **create_quest_schedule_request** | [**CreateQuestScheduleRequest**](CreateQuestScheduleRequest.md)|  | 

### Return type

[**CreateQuestSchedule200Response**](CreateQuestSchedule200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_user**
> User get_external_user(key, external_id, game_id)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.user import User
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.ExternalApi(api_client)
    key = 'key_example' # str | 
    external_id = 'external_id_example' # str | 
    game_id = 'game_id_example' # str | 

    try:
        api_response = api_instance.get_external_user(key, external_id, game_id)
        print("The response of ExternalApi->get_external_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->get_external_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **external_id** | **str**|  | 
 **game_id** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_goals**
> List[Goal] get_my_goals(api_key)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.goal import Goal
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.ExternalApi(api_client)
    api_key = 'api_key_example' # str | given by the Ledge admins.

    try:
        api_response = api_instance.get_my_goals(api_key)
        print("The response of ExternalApi->get_my_goals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->get_my_goals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| given by the Ledge admins. | 

### Return type

[**List[Goal]**](Goal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | quests created by this api key |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_quests**
> List[Quest] get_my_quests(api_key)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.quest import Quest
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.ExternalApi(api_client)
    api_key = 'api_key_example' # str | given by the Ledge admins.

    try:
        api_response = api_instance.get_my_quests(api_key)
        print("The response of ExternalApi->get_my_quests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->get_my_quests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| given by the Ledge admins. | 

### Return type

[**List[Quest]**](Quest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | quests created by this api key |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> User register_user(key, external_user)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.external_user import ExternalUser
from ledge_python_sdk.models.user import User
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.ExternalApi(api_client)
    key = 'key_example' # str | 
    external_user = ledge_python_sdk.ExternalUser() # ExternalUser | 

    try:
        api_response = api_instance.register_user(key, external_user)
        print("The response of ExternalApi->register_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->register_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **external_user** | [**ExternalUser**](ExternalUser.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_activity**
> TrackActivity200Response track_activity(key, external_activity)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.external_activity import ExternalActivity
from ledge_python_sdk.models.track_activity200_response import TrackActivity200Response
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.ExternalApi(api_client)
    key = 'key_example' # str | 
    external_activity = ledge_python_sdk.ExternalActivity() # ExternalActivity | 

    try:
        api_response = api_instance.track_activity(key, external_activity)
        print("The response of ExternalApi->track_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->track_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **external_activity** | [**ExternalActivity**](ExternalActivity.md)|  | 

### Return type

[**TrackActivity200Response**](TrackActivity200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

