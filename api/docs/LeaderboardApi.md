# ledge_python_sdk.LeaderboardApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_leaderboard**](LeaderboardApi.md#get_current_leaderboard) | **GET** /leaderboard | 
[**get_ranks**](LeaderboardApi.md#get_ranks) | **GET** /leaderboard/ranks | 
[**get_user_rank**](LeaderboardApi.md#get_user_rank) | **GET** /leaderboard/userRank | 


# **get_current_leaderboard**
> Leaderboard get_current_leaderboard(game_id)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.leaderboard import Leaderboard
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
    api_instance = ledge_python_sdk.LeaderboardApi(api_client)
    game_id = 'game_id_example' # str | 

    try:
        api_response = api_instance.get_current_leaderboard(game_id)
        print("The response of LeaderboardApi->get_current_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardApi->get_current_leaderboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**|  | 

### Return type

[**Leaderboard**](Leaderboard.md)

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

# **get_ranks**
> PaginatedRankDetailed get_ranks(leaderboard_id, page=page, limit=limit)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.paginated_rank_detailed import PaginatedRankDetailed
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
    api_instance = ledge_python_sdk.LeaderboardApi(api_client)
    leaderboard_id = 'leaderboard_id_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 10 # float |  (optional) (default to 10)

    try:
        api_response = api_instance.get_ranks(leaderboard_id, page=page, limit=limit)
        print("The response of LeaderboardApi->get_ranks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardApi->get_ranks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboard_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] [default to 10]

### Return type

[**PaginatedRankDetailed**](PaginatedRankDetailed.md)

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

# **get_user_rank**
> RankDetailed get_user_rank(external_id, leaderboard_id)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.models.rank_detailed import RankDetailed
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
    api_instance = ledge_python_sdk.LeaderboardApi(api_client)
    external_id = 'external_id_example' # str | 
    leaderboard_id = 'leaderboard_id_example' # str | 

    try:
        api_response = api_instance.get_user_rank(external_id, leaderboard_id)
        print("The response of LeaderboardApi->get_user_rank:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardApi->get_user_rank: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 
 **leaderboard_id** | **str**|  | 

### Return type

[**RankDetailed**](RankDetailed.md)

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

