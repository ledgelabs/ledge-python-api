# ledge_python_sdk.QuestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_goal_streak**](QuestsApi.md#get_goal_streak) | **GET** /quests/goal-streak | 
[**get_last_refreshed_at**](QuestsApi.md#get_last_refreshed_at) | **GET** /quests/refreshedAt | 
[**get_participants**](QuestsApi.md#get_participants) | **GET** /quests/participants | 
[**get_past_winners**](QuestsApi.md#get_past_winners) | **GET** /quests/{questId}/past-winners | 
[**get_quests**](QuestsApi.md#get_quests) | **GET** /quests | 
[**is_participating**](QuestsApi.md#is_participating) | **GET** /quests/{goalId}/is-participating | 


# **get_goal_streak**
> float get_goal_streak(goal_id, start_time=start_time, end_time=end_time, quest_schedule_id=quest_schedule_id)



A streak activates when the user achieves the goal target.

### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.QuestsApi(api_client)
    goal_id = 'goal_id_example' # str | 
    start_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    quest_schedule_id = 'quest_schedule_id_example' # str |  (optional)

    try:
        api_response = api_instance.get_goal_streak(goal_id, start_time=start_time, end_time=end_time, quest_schedule_id=quest_schedule_id)
        print("The response of QuestsApi->get_goal_streak:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestsApi->get_goal_streak: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 
 **start_time** | **datetime**|  | [optional] 
 **end_time** | **datetime**|  | [optional] 
 **quest_schedule_id** | **str**|  | [optional] 

### Return type

**float**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | number indicating most recent consecutive streak |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_refreshed_at**
> datetime get_last_refreshed_at(object_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.QuestsApi(api_client)
    object_id = 'object_id_example' # str | 

    try:
        api_response = api_instance.get_last_refreshed_at(object_id)
        print("The response of QuestsApi->get_last_refreshed_at:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestsApi->get_last_refreshed_at: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 

### Return type

**datetime**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participants**
> List[User] get_participants(goal_id, limit=limit, distinct_user=distinct_user)



### Example

* Api Key Authentication (api_key):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.QuestsApi(api_client)
    goal_id = 'goal_id_example' # str | 
    limit = 3.4 # float |  (optional)
    distinct_user = True # bool |  (optional)

    try:
        api_response = api_instance.get_participants(goal_id, limit=limit, distinct_user=distinct_user)
        print("The response of QuestsApi->get_participants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestsApi->get_participants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 
 **limit** | **float**|  | [optional] 
 **distinct_user** | **bool**|  | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_past_winners**
> List[UserQuestDrawDetailed] get_past_winners(quest_id, start_date=start_date, end_date=end_date)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.user_quest_draw_detailed import UserQuestDrawDetailed
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.QuestsApi(api_client)
    quest_id = 'quest_id_example' # str | 
    start_date = 'start_date_example' # str |  (optional)
    end_date = 'end_date_example' # str |  (optional)

    try:
        api_response = api_instance.get_past_winners(quest_id, start_date=start_date, end_date=end_date)
        print("The response of QuestsApi->get_past_winners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestsApi->get_past_winners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quest_id** | **str**|  | 
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 

### Return type

[**List[UserQuestDrawDetailed]**](UserQuestDrawDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quests**
> PaginatedQuestScheduleDetailed get_quests(page=page, limit=limit, quest_type=quest_type, object_id=object_id, activity_types=activity_types)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.activity_type import ActivityType
from ledge_python_sdk.models.paginated_quest_schedule_detailed import PaginatedQuestScheduleDetailed
from ledge_python_sdk.models.quest_type import QuestType
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.QuestsApi(api_client)
    page = 0 # float |  (optional) (default to 0)
    limit = 10 # float |  (optional) (default to 10)
    quest_type = ledge_python_sdk.QuestType() # QuestType |  (optional)
    object_id = 'object_id_example' # str |  (optional)
    activity_types = [ledge_python_sdk.ActivityType()] # List[ActivityType] |  (optional)

    try:
        api_response = api_instance.get_quests(page=page, limit=limit, quest_type=quest_type, object_id=object_id, activity_types=activity_types)
        print("The response of QuestsApi->get_quests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestsApi->get_quests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] [default to 10]
 **quest_type** | [**QuestType**](.md)|  | [optional] 
 **object_id** | **str**|  | [optional] 
 **activity_types** | [**List[ActivityType]**](ActivityType.md)|  | [optional] 

### Return type

[**PaginatedQuestScheduleDetailed**](PaginatedQuestScheduleDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_participating**
> bool is_participating(goal_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.QuestsApi(api_client)
    goal_id = 'goal_id_example' # str | 

    try:
        api_response = api_instance.is_participating(goal_id)
        print("The response of QuestsApi->is_participating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestsApi->is_participating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 

### Return type

**bool**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

